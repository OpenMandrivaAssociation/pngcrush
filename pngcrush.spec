Summary:	Utility to compress PNG files
Name:		pngcrush
Version:	1.7.32
Release:	1
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/project/pmt/pngcrush/%{version}/%{name}-%{version}.tar.gz
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep

%setup -q -n %{name}-%{version}

%build
# force using system headers
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h
pngflags=$(pkg-config --cflags --libs libpng)

gcc %{optflags} %{ldflags} -o pngcrush pngcrush.c $pngflags -lz -lm

%install
mkdir -p %{buildroot}%{_bindir}

install -m 0755 pngcrush %{buildroot}%{_bindir}
chmod 644 ChangeLog*

%files 
%doc ChangeLog.html
%{_bindir}/*
