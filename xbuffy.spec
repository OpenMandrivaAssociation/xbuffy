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
BuildRequires:	libxaw-devel
BuildRequires:	libxt-devel
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

