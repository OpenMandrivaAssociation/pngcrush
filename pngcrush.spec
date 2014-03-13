Summary:	Utility to compress PNG files
Name:		pngcrush
Version:	1.7.72
Release:	1
License:	zlib
Group:		Graphics
URL:		http://pmt.sourceforge.net/%{name}/
Source0:	http://downloads.sourceforge.net/project/pmt/%{name}/%{version}/%{name}-%{version}.tar.xz
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can
compress them as much as 40% losslessly.

%prep

%setup -q -n %{name}-%{version}

%build
# force using system headers
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h
pngflags=$(pkg-config --cflags --libs libpng)

%{__cc} %{optflags} %{ldflags} -o pngcrush pngcrush.c $pngflags -lz -lm

%install
mkdir -p %{buildroot}%{_bindir}

install -m 0755 pngcrush %{buildroot}%{_bindir}
chmod 644 ChangeLog*

%files 
%doc ChangeLog.html
%{_bindir}/*


%changelog
* Tue Jul 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.32-1
+ Revision: 810879
- version update 1.7.32

* Thu Jul 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.31-1
+ Revision: 808997
- version update 1.7.31

* Fri Jun 01 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.27-1
+ Revision: 801668
- version update 1.7.27

* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.24-1
+ Revision: 760321
- version update 1.7.24

* Sat Sep 03 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.16-1
+ Revision: 698151
- update to new version 1.7.16

* Sat Jul 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.10-1mdv2011.0
+ Revision: 550137
- update to new version 1.7.10

* Fri Feb 12 2010 Colin Guthrie <cguthrie@mandriva.org> 1.7.2-2mdv2010.1
+ Revision: 504924
- Compile against current libpng

* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.2-1mdv2010.0
+ Revision: 440760
- update to new version 1.7.2

* Sat Jul 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-1mdv2010.0
+ Revision: 397188
- 1.7.0
- use the nolib source

* Sun Jun 07 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6.19-1mdv2010.0
+ Revision: 383710
- 1.6.19

* Wed Jun 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1.6.17-1mdv2010.0
+ Revision: 382514
- update to new version 1.6.17

* Fri May 08 2009 Funda Wang <fwang@mandriva.org> 1.6.16-1mdv2010.0
+ Revision: 373383
- New version 1.6.16

* Thu Mar 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.6.15-1mdv2009.1
+ Revision: 349136
- update to new version 1.6.15

* Mon Feb 23 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6.14-1mdv2009.1
+ Revision: 344093
- 1.6.14
- build against system libs (thanks fedora)

* Thu Jan 08 2009 Thierry Vignaud <tv@mandriva.org> 1.6.13-2mdv2009.1
+ Revision: 327213
- make doc readable

* Thu Jan 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.6.13-1mdv2009.1
+ Revision: 327212
- update to new version 1.6.13

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 1.6.11-1mdv2009.1
+ Revision: 304471
- update to new version 1.6.11

* Tue Aug 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.10-1mdv2009.0
+ Revision: 276301
- update to new version 1.6.10
- spec file clean
- update to new version 1.6.7
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Thu May 22 2008 Frederik Himpe <fhimpe@mandriva.org> 1.6.6-1mdv2009.0
+ Revision: 210091
- New version
- Fix license
- Use sed hack to use Mandriva's default gcc, CFLAGS and LDFLAGS
- A few SPEC clean-ups

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 1.6.4-1mdv2008.0
+ Revision: 21511
- update to 1.6.4

