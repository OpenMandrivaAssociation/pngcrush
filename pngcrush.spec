%define name pngcrush
%define version 1.6.3
%define release %mkrel 2

Name: %{name}
Summary: Utility to compress pngs
Version: %{version}
Release: %{release}
Source: http://ovh.dl.sourceforge.net/sourceforge/pmt/%{name}-%{version}.tar.bz2
Patch0: pngcrush-1.5.9-shared-zlib.patch
Group: Graphics
URL: http://pmt.sourceforge.net/pngcrush/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Buildrequires: zlib-devel

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
#%patch0 -p1

%build

%make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 pngcrush $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
#%doc INSTALL.txt README.txt
%{_bindir}/*


