# rpmbuild

 Use at your own risk.

# useful tips


## getting source tarball

````
#spectool -g -R specfile
spectool -g -R ./SPECS/nasm.spec
````

## dunno which package provides `spectool`

````
# if you are using yum as package manager
yum provides spectool
````

## getting source rpm

````
#yumdownloader --source [package name]
yumdownloader --source nasm
````

## extracting rpm

````
#rpm2cpio rpm_file|cpio --extract

````

## gcc is whining

Maybe your gcc is just too old. install devtoolset-6 and try again.

````
# to enable
scl enable devtoolset-6 bash
gcc --version
````

## rpmbuild -bb says it needs more packages!!!

````
# install that packages like
# sudo yum -y install `rpmbuild -bb SPEC_FILE |& sed '1d'|cut -d ' ' -f 1|sed 's/\t//'`
sudo yum -y install `rpmbuild -bb ./SPECS/obs-studio.spec |& sed '1d'|cut -d ' ' -f 1|sed 's/\t//'`

````

## nasm

[SourceCode Pro font](https://www.fontsquirrel.com/fonts/source-sans-pro)

````
wget https://www.fontsquirrel.com/fonts/download/source-sans-pro
mkdir sp
unzip source-sans-pro.zip -d ./sp
sudo mv ./sp /usr/share/fonts/
sudo fc-cache -f
````

### libarchive-devel 
 
libarchive-devel is in rhel-7-server-optional-rpms which is disabled by default.

# perl stuff

````
yum -y install perl-Sort-Versions perl-Font*
````

# useful notes

 - You need at least 2.13 of nasm to compile x264

