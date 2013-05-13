%define name xbuffy
%define version 3.4
%define release %mkrel 13

Summary:	X-based multiple mailbox biff
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Graphical desktop/Other
Source:		%{name}-%{version}.tar.bz2
Url:		ftp://ftp.virginia.edu:/pub/xbuffy/
Patch0:		xbuffy-3.4-multiple-box.patch
Patch1:		xbuffy-nntp-gcc331.patch
Buildrequires:	libx11-devel
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Xbuffy is a program that watches multiple mailboxes and newsgroups
and displays a count of new mail or news, and optionally displays a pop-up
window containing the From: and Subject: lines when new mail or news
arrives.  Xbuffy can also run a program (such as a xterm with your mail reader)
when you click on the mailbox.  

%prep
%setup -q
%patch0
%patch1

%build
%configure2_5x --enable-nntp --enable-content-length
%make

%install
rm -fr %buildroot
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}/
install -s -m 755  xbuffy $RPM_BUILD_ROOT%{_bindir}/xbuffy
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 xbuffy.1 $RPM_BUILD_ROOT%{_mandir}/man1/xbuffy.1x
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/
install -m 644  XBuffy.ad $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/XBuffy

%files
%defattr(-,root,root)
%doc ChangeLog README README.imap README.cclient boxfile.fmt boxfile.sample
%{_bindir}/xbuffy
%{_mandir}/man1/xbuffy.1x*
%{_datadir}/X11/app-defaults/XBuffy

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.4-13mdv2011.0
+ Revision: 634881
- bunzip2 the patches
- use standard prefix

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.4-12mdv2010.0
+ Revision: 445892
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 3.4-11mdv2009.0
+ Revision: 262259
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 3.4-10mdv2009.0
+ Revision: 256630
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 3.4-8mdv2008.1
+ Revision: 118975
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import xbuffy


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.4-8mdk
- Rebuild

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 3.4-7mdk
- clean header
- fix gcc 3.3.1 compil

* Mon Apr 28 2003 Warly <warly@mandrakesoft.com> 3.4-6mdk
- fix buildrequires

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 3.4-5mdk
- rebuild

* Wed Apr 25 2001 Warly <warly@mandrakesoft.com> 3.4-4mdk
- Add subbox title in mail displaying

* Mon Apr 23 2001 Warly <warly@mandrakesoft.com> 3.4-3mdk
- does not stop working with empty boxfiles.

* Sat Dec 23 2000 Warly <warly@mandrakesoft.com> 3.4-2mdk
- add a patch to put multiple file in the same box

* Tue Aug 29 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.4-1mdk
- first Mandrake release.
