%define name xbuffy
%define version 3.4
%define release %mkrel 10

Summary:	X-based multiple mailbox biff
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Graphical desktop/Other
Source:		%{name}-%{version}.tar.bz2
Url:		ftp://ftp.virginia.edu:/pub/xbuffy/
Patch0:		xbuffy-3.4-multiple-box.patch.bz2
Patch1:		xbuffy-nntp-gcc331.patch.bz2
Buildrequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Xbuffy is a program that watches multiple mailboxes and newsgroups
and displays a count of new mail or news, and optionally displays a pop-up
window containing the From: and Subject: lines when new mail or news
arrives.  Xbuffy can also run a program (such as a xterm with your mail reader)
when you click on the mailbox.  

%prep

%setup

#%patch0 -p1 -b .warly
%patch0
%patch1

%build
 
CONF_OPTS="--enable-nntp --enable-content-length"

if [ -d /usr/local/src/imap ] ; then
   %configure --with-cclient=/usr/local/src/imap $CONF_OPTS
else
   %configure $CONF_OPTS
fi

%make

%install

install -m 755 -d $RPM_BUILD_ROOT/usr/X11R6/bin/
install -s -m 755  xbuffy $RPM_BUILD_ROOT/usr/X11R6/bin/xbuffy
install -m 755 -d $RPM_BUILD_ROOT/usr/X11R6/man/man1/
install -m 644 xbuffy.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1/xbuffy.1x
install -m 755 -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/
install -m 644  XBuffy.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XBuffy
%files
%defattr(-,root,root)
%attr(-,root,root) /usr/X11R6/bin/xbuffy
%attr(-,root,root) /usr/X11R6/man/man1/xbuffy.1x*
%attr(-,root,root) /usr/X11R6/lib/X11/app-defaults/XBuffy
%doc ChangeLog README README.imap README.cclient boxfile.fmt boxfile.sample

%clean
rm -rf $RPM_BUILD_ROOT

