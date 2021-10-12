Summary:	Utility to compress PNG files
Name:		pngcrush
Version:	1.8.13
Release:	3
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/pmt/%{name}-%{version}-nolib.tar.xz
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep
%autosetup -n %{name}-%{version}-nolib -p1

%build
%set_build_flags
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags} $(pkg-config --cflags --libs libpng zlib) -lm"

%install
install -m0755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files 
%doc ChangeLog.html
%{_bindir}/%{name}
