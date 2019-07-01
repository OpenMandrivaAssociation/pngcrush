Summary:	Utility to compress PNG files
Name:		pngcrush
Version:	1.8.13
Release:	3
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/project/pmt/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep
%autosetup -p1
# force using system headers
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h
chmod og+r *

%build
%setup_compile_flags
%make_build CFLAGS="%{optflags}" LDFLAGS="%{ldflags} $(pkg-config --cflags --libs libpng zlib) -lm"

%install
install -m0755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files 
%doc ChangeLog.html
%{_bindir}/%{name}
