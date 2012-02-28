#!/usr/bin/env python
# coding:utf-8

"WxPython class and function source code browser"

__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0"

import wx
import os.path
import pyclbr

from threading import Thread, Event, Lock, Semaphore

import images


def find_functions_and_classes(modulename, path):
    """Parse the file and return [('lineno', 'class name', 'function')]
    
    >>> with open("test1.py", "w") as f:
    ...  f.write("def hola():\n pass\n#\ndef chau(): pass\n")
    ...  f.write("class Test:\n def __init__():\n\n  pass\n")
    >>> results = find_functions_and_classes("test1", ".")
    >>> results
    [[1, None, 'hola'], [3, None, 'chau'], [5, 'Test', '__init__']]
    
    """
    # Assumptions: there is only one function/class per line (syntax)
    #              class attributes & decorators are ignored
    #              imported functions should be ignored
    #              inheritance clases from other modules is unhandled (super)doctest for results failed, exception NameError("name 'results' is not defined",)

    result = []
    # delete the module if parsed previously:
    if modulename in pyclbr._modules:
        del pyclbr._modules[modulename]
    module = pyclbr.readmodule_ex(modulename, path=path and [path])
    for obj in module.values():
        if isinstance(obj, pyclbr.Function) and obj.module == modulename:
            # it is a top-level global function (no class)
            result.append([obj.lineno, None, obj.name])
        elif isinstance(obj, pyclbr.Class) and obj.module == modulename:
            # it is a class, look for the methods:
            result.append([obj.lineno, obj.name, None])
            for method, lineno in obj.methods.items():
                result.append([lineno, obj.name, method])
    return result


EVT_PARSED_ID = wx.NewId()
EVT_EXPLORE_ID = wx.NewId()
    

class ExplorerEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, event_type, data=None):
        wx.PyEvent.__init__(self)
        self.SetEventType(event_type)
        self.data = data


class Explorer(Thread):
    "Worker thread to analyze a python source file"

    def __init__(self, parent=None, modulename=None, filepath=None):
        Thread.__init__(self)
        self.parent = parent
        self.modulename = modulename
        self.filepath = filepath
        self.start()                # creathe the new thread

    def run(self):
        items = find_functions_and_classes(self.modulename, self.filepath)
        event = ExplorerEvent(EVT_PARSED_ID, 
                              (self.modulename, self.filepath, items))
        wx.PostEvent(self.parent, event)


class ExplorerTreeCtrl(wx.TreeCtrl):

    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

    def OnCompareItems(self, item1, item2):
        # sort by pydata (lineno)
        t1 = self.GetItemPyData(item1)
        t2 = self.GetItemPyData(item2)
        if t1 < t2: return -1
        if t1 == t2: return 0
        return 1


class ExplorerPanel(wx.Panel):
    def __init__(self, parent):
        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.parent = parent
        self.working = False
        self.modules = {}

        tID = wx.NewId()

        self.tree = ExplorerTreeCtrl(self, tID, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT,
                               )

        il = wx.ImageList(16, 16)
        self.images = {
            'module': il.Add(images.module.GetBitmap()),
            'class': il.Add(images.class_.GetBitmap()),
            'function': il.Add(images.function.GetBitmap()),
            'method': il.Add(images.method.GetBitmap()),
            }
    
        self.tree.SetImageList(il)
        self.il = il
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.tree.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.root = self.tree.AddRoot("")
        self.tree.SetPyData(self.root, None)

        self.Connect(-1, -1, EVT_PARSED_ID, self.OnParsed)

    def ParseFile(self, fullpath, refresh=False):
        if self.working:
            wx.Bell()
        else:
            self.working = True
            filepath, filename = os.path.split(fullpath)
            modulename, ext = os.path.splitext(filename)
            self.filename = fullpath
            # if module not already in the tree, add it
            if (modulename, filepath) not in self.modules:
                if refresh:
                    # do not rebuild if user didn't "explored" it previously
                    self.working = False
                    return
                module = self.tree.AppendItem(self.root, modulename)
                self.modules[(modulename, filepath)] = module
                self.tree.SetPyData(module, (self.filename, 1))
                self.tree.SetItemImage(module, self.images['module'])
            else:
                module = self.modules[(modulename, filepath)]
                self.tree.CollapseAndReset(module)
            self.tree.SetItemText(module, "%s (loading...)" % modulename)
            # Start worker thread
            thread = Explorer(self, modulename, filepath)
    
    def OnParsed(self, evt):
        modulename, filepath, items = evt.data
        module = self.modules[(modulename, filepath)]
        self.tree.SetItemText(module, modulename)
        self.tree.SelectItem(module)
        classes = {}
        for lineno, class_name, function_name in items:
            if class_name is None:
                child = self.tree.AppendItem(module, function_name)
                self.tree.SetItemImage(child, self.images['function'])
            elif function_name is None:
                child = self.tree.AppendItem(module, class_name)
                self.tree.SetItemImage(child, self.images['class'])
                classes[class_name] = child
            else:
                child = self.tree.AppendItem(classes[class_name], function_name)
                self.tree.SetItemImage(child, self.images['method'])

            self.tree.SetPyData(child, (self.filename, lineno))

        self.tree.SortChildren(module)    
        self.tree.Expand(module)
        self.working = False

    def OnItemExpanded(self, event):
        item = event.GetItem()
        if item:
            self.tree.SortChildren(item)  

    def OnLeftDClick(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:
            filename, lineno = self.tree.GetItemPyData(item)
            event = ExplorerEvent(EVT_EXPLORE_ID, 
                              (filename, lineno))
            wx.PostEvent(self.parent, event)
        event.Skip()

    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        self.tree.SetDimensions(0, 0, w, h)


class TestFrame(wx.Frame):

    def __init__(self, filename=None):
        wx.Frame.__init__(self, None)
        self.Show()
        self.panel = ExplorerPanel(self)
        self.panel.ParseFile(__file__)
        self.panel.ParseFile(__file__)
        self.SendSizeEvent() 


if __name__ == '__main__':
    
    def main():
        app = wx.App()
        frame = TestFrame()
        app.MainLoop()
    
    main()