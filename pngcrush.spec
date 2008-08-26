Name:		pngcrush
Summary:	Utility to compress PNG files
Version:	1.6.10
Release:	%mkrel 1
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/pmt/%{name}-%{version}.tar.lzma
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep

%setup -q

# Use Mandriva's default gcc, CFLAGS and LDFLAGS
sed -i -e "s/gcc-4.3.0/gcc/" Makefile
# -e "/CFLAGS/d" -e "/LDFLAGS/d" Makefile

%build

%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 pngcrush %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
%doc ChangeLog.txt
%{_bindir}/*
