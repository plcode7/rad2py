# ide2py #

![http://rad2py.googlecode.com/hg/screenshots/ide2py-0.05-ubuntu.png](http://rad2py.googlecode.com/hg/screenshots/ide2py-0.05-ubuntu.png)

This screenshot shows basic capabilities of the IDE:

  * Debugger in action (current line 18, breakpoint at the same line)
  * Repository showing a web2py clone
  * Browser on tested page
  * Shell changing a variable value
  * Some PSP found defect and time counters


## wxPyDiff ##

Internal tool to show differences (against the repository or against a reused program):

![http://rad2py.googlecode.com/hg/screenshots/wxPyDiff.png](http://rad2py.googlecode.com/hg/screenshots/wxPyDiff.png)

This is used to show new, modified an deleted lines (that will be accounted in the historic database for further estimation purposes)

## Pytong (unittest gui) ##

Visual Unit Test interface, showing test suites execution and result:

![http://rad2py.googlecode.com/hg/screenshots/pytong.png](http://rad2py.googlecode.com/hg/screenshots/pytong.png)

## psp support ##

### Toolbar ###

Current project selection, time recording controls (start, pause, stop), elapsed time progress bar, new defect and run check buttons:

![http://rad2py.googlecode.com/hg/screenshots/psp_toolbar.png](http://rad2py.googlecode.com/hg/screenshots/psp_toolbar.png)

### Time and Defects panels ###

PSP time delta grid per phase (planned, actual and interruption, with comments):

![http://rad2py.googlecode.com/hg/screenshots/psp_plan_summary_times.png](http://rad2py.googlecode.com/hg/screenshots/psp_plan_summary_times.png)

PSP defects list (with a checkbox to mark fixed defects):

![http://rad2py.googlecode.com/hg/screenshots/psp_defects.png](http://rad2py.googlecode.com/hg/screenshots/psp_defects.png)

### PSP Defect Dialog ###

![http://rad2py.googlecode.com/hg/screenshots/psp_defect.png](http://rad2py.googlecode.com/hg/screenshots/psp_defect.png)

### PSP Metadata ###

PSP phase per line, to detect defect injection phase:

![http://rad2py.googlecode.com/hg/screenshots/psp_metadata.png](http://rad2py.googlecode.com/hg/screenshots/psp_metadata.png)

### PSP Wiki ###

A basic Electronic Process Guide (EPG):

![http://rad2py.googlecode.com/hg/screenshots/psp_wiki.png](http://rad2py.googlecode.com/hg/screenshots/psp_wiki.png)

# psp2py #

PSP projects CRUD (title, description, requerimients, testing, LOC estimated and actual metrics, defects and times, etc.):

![http://rad2py.googlecode.com/hg/screenshots/psp_project.png](http://rad2py.googlecode.com/hg/screenshots/psp_project.png)

## PROBE Estimation ##

PSP PROBE (PROxy Based Estimation) of projected objects size (classes/functions):

![http://rad2py.googlecode.com/hg/screenshots/psp_probe.png](http://rad2py.googlecode.com/hg/screenshots/psp_probe.png)

PSP time estimation using linear regression and prediction intervals:

![http://rad2py.googlecode.com/hg/screenshots/psp_estimate.png](http://rad2py.googlecode.com/hg/screenshots/psp_estimate.png)

PSP Projects Reuse Library (historic data of developed objects -classes and functions- for PROBE):

![http://rad2py.googlecode.com/hg/screenshots/psp_reuse_library.png](http://rad2py.googlecode.com/hg/screenshots/psp_reuse_library.png)

## Reports ##

PSP General measures report (productivity, defect removal efficiency, cost of quality):

![http://rad2py.googlecode.com/hg/screenshots/psp_reports.png](http://rad2py.googlecode.com/hg/screenshots/psp_reports.png)

PSP Defect Type Standard Report (errors classification for process improvement):

![http://rad2py.googlecode.com/hg/screenshots/psp_defect_report.png](http://rad2py.googlecode.com/hg/screenshots/psp_defect_report.png)

PSP Projects Summary Report (errors classification for process improvement):

![http://rad2py.googlecode.com/hg/screenshots/psp_report_projects.png](http://rad2py.googlecode.com/hg/screenshots/psp_report_projects.png)

# Graphs & Charts #

Linear regression of historic data (development time estimation):

![http://rad2py.googlecode.com/hg/screenshots/psp_linear_regression.png](http://rad2py.googlecode.com/hg/screenshots/psp_linear_regression.png)

Log-normal distribution of object sizes (used for size -loc- estimation):

![http://rad2py.googlecode.com/hg/screenshots/psp_normal_distribution.png](http://rad2py.googlecode.com/hg/screenshots/psp_normal_distribution.png)

Pareto Distribution chart to show most common error types (to improve the review phase):

![http://rad2py.googlecode.com/hg/screenshots/psp_pareto_distribution.png](http://rad2py.googlecode.com/hg/screenshots/psp_pareto_distribution.png)

Defect by phase (categorization and average fix type):

![http://rad2py.googlecode.com/hg/screenshots/psp_average_fix_times.png](http://rad2py.googlecode.com/hg/screenshots/psp_average_fix_times.png)