Summary:	Utility to compress PNG files
Name:		pngcrush
Version:	1.7.85
Release:	1
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/project/pmt/%{name}/%{version}/%{name}-%{version}.tar.xz
Buildrequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep
%setup -q
# force using system headers
rm z*.h crc32.h deflate.h inf*.h trees.h png*.h
chmod og+r *

%build
%{__cc} %{optflags} -O3 -funroll-loops -fomit-frame-pointer -Wall -Wshadow %{ldflags} -o pngcrush pngcrush.c $(pkg-config --cflags --libs libpng zlib) -lm

%install
install -m0755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files 
%doc ChangeLog.html
%{_bindir}/%{name}
