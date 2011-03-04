Information sources used
---

[Brandon Rhodes' buildout article](http://rhodesmill.org/brandon/buildout/)

[Chapters 5-7 of Expert Python Programming Book, Packt Publishing, 2008 by Tarek Ziadé]

[The first three chapters of Python Geospatial Development, Packt Publishing, 2010 by Erik Westra]

Shure you need python in your systems search path... (tested with version 2.6).

Initially I created a `buildout.cfg` file in this READMEs folder.

In a folder `.buildout` in my home directory - see Brandons page: "How can I avoid having every buildout on my system download a separate copy of each egg it needs?" (on mswin the `%USERPROFILE%` should also do, not tested though) I have a `default.cfg` file telling buildout to download only packages not in the specified eggs directory already, contents (adapt the path):

    [buildout]
    eggs-directory = h:/.homedir/eggs

The app logic I created for proving concept is mashed up from Eriks books examples, pp. 41 and 57. The apps structure (organisation of app and test sources, contents organisation in `setup.py` file and main purposes of all those) is modeled after pp. 143-165 in Tareks book ([the sources are here](https://bitbucket.org/tarek/atomisator)).

I created a `Manifest.in` file whose aim was to package the data files for distribution (is the needed preparation for the `dist` command), infos see [here](TODO). For this aim I also have the `include_package_data` clause in the `setup.py` file.

Next made a folder `src` with the package folder in it (package name as in buildout.cfg, in our case `python_package_example`) and in that package folder the "main" `__init__.py` file and a file (`tests.py`) with some method(s) specifing tests to run. Our program(s) will use some data at runtime to read in and analse. As I found it too big for duplication, let this as a task for you to load it. Install wget for your system [\*]. Now load the data archive and unpack it with your systems app for zip files  (see p. 39 in Eriks book):

    wget -c -Psrc/python_package_example/data -- http://www2.census.gov/geo/tiger/TIGER2009/tl_2009_us_state.zip

Afterwards unpacking you may delete the zip archive.

You'll have to load the [bootstrap.py (latest version)](http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py) file into this READMEs folder:

    wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

You could now run a new prompt (e. g. `cmd` on mswin) or use the already open and trigger:

    python bootstrap.py
    ./bin/buildout

Those calls will generate and load the needed library files and generate the binaries. To run the generated binaries from the apps sources:

    ./bin/do_osgeo
    ./bin/do_pyproj

Each time you change the sources you'll need to run `./bin/buildout` again.

You need the packages (tested with those versions and python 2.6 on win32):
---

 * GDAL-1.6.1
 * pyproj-1.8.8

For downloads and installation how-tos (for only trying out the app you'll only need the GDAL library steps) go here http://pypi.python.org/pypi/pyproj/1.8.8 and here http://pypi.python.org/pypi/GDAL/1.6.1. For the GDAL library on mswin32 you only need to append the `bin` folders full path of gdal distribution to your systems search path and to add a new environment variable `GDAL_DATA` pointing to the `data` folder of the gdal distribution (full path). The GDAL bindings and pyproj are automatically installed to the `eggs` folder (remember the `~/.buildout/default.cfg` file shown above?!) by this examples configuration, the variables in my setup are similar to:

    GDAL_DATA=E:\test\gdalwin32-1.6\data
    PATH=[...;]E:\test\gdalwin32-1.6\bin[;...]

With unix there should be almost no problem as easy_install should be able to install the dependencies.

Note to myself (if you're curious for more GIS-hacking)
---

Eriks book also has a mapnik example, for which I installed the mapnik library and appended its `bin` folder's location to the `PATH` environment variable too. Not to forget to update the `PYTHONPATH` variable I have (under ["Manual Instructions" here](http://trac.mapnik.org/wiki/WindowsInstallation)):

    PYTHONPATH=e:\test\mapnik-0.7.1\python\2.6\site-packages;C:\Dokumente und Einstellungen\myuser\Anwendungsdaten\Python26\lib\site-packages

[\*] You also might install the mingw tool chain + msys with mingw-get-inst, start it's preconfigured prompt (`msys.bat`) and install `wget` (`mingw-get install msys-wget`).

vim: filetype=markdown
