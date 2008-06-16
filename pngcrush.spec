Name:		pngcrush
Summary:	Utility to compress pngs
Version:	1.6.7
Release:	%mkrel 1
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/pmt/%{name}-%{version}.tar.lzma
Buildrequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep

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
