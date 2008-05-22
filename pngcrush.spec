%define name pngcrush
%define version 1.6.6
%define rel 1

Name: %{name}
Summary: Utility to compress pngs
Version: %{version}
Release: %mkrel %{rel}
Source: http://ovh.dl.sourceforge.net/sourceforge/pmt/%{name}-%{version}.tar.lzma
Group: Graphics
URL: http://pmt.sourceforge.net/pngcrush/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: zlib
Buildrequires: zlib-devel

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
# Use Mandriva's default gcc, CFLAGS and LDFLAGS
sed -i -e "s/gcc-4.3.0/gcc/" -e "/CFLAGS/d" -e "/LDFLAGS/d" Makefile

%build

%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 pngcrush %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
#%doc INSTALL.txt README.txt
%{_bindir}/*
