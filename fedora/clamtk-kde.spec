Name: clamtk-kde
Version: 0.15
Release: 1.fc
Summary: Plugin to allow right-click virus-scanning from within KDE
License: GPL+ or Artistic 2.0
Group: System Environment/Shells
URL: http://code.google.com/p/clamtk/

Source: https://bitbucket.org/dave_theunsub/clamtk-kde/downloads/clamtk-kde-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: clamtk >= 4.00, kde-filesystem

%description
ClamTk is a front-end for ClamAV anti-virus.
This plugin allows users to right-click on files and directories
from within KDE and utilize the ClamTk front-end for virus scanning.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%{__install} -D -m0644 clamtk-kde.xpm %{buildroot}%{_datadir}/pixmaps/clamtk-kde.xpm
%{__install} -D -m0644 clamtk-kde.desktop %{buildroot}%{_datadir}/kde4/services/clamtk-kde.desktop
%{__install} -D -m0644 clamtk-kde.1.gz %{buildroot}%{_mandir}/man1/clamtk-kde.1.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README LICENSE CHANGES
%{_datadir}/kde4/services/*.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 0.15-1.fc
- Upgraded to 0.15.
- Requirement is now kde-filesystem.
- Updated Url and Source.
- Updated License to Artistic 2.0.

* Sat May 23 2009 Dave M. <dave.nerd@gmail.com> - 0.14-1.fc
- Upgraded to 0.14.
- Updated kdebase requirement to > 4.0.0.
- Updated filepath to kde4 structure.

* Sun Apr 12 2009 Dave M. <dave.nerd@gmail.com> - 0.13-1.fc
- Upgraded to 0.13.

* Sun Mar 22 2009 Dave M. <dave.nerd@gmail.com> - 0.12-1.fc
- Upgraded to 0.12.
- Minimum clamtk version now 4.00.

* Wed Aug 27 2008 Dave M. <dave.nerd@gmail.com> - 0.11-1.fc
- Upgraded to 0.11.

* Thu Jun 12 2008 Dave M. <dave.nerd@gmail.com> - 0.10-1.fc
- Upgraded to 0.10.

* Tue Feb 5 2008 Dave M. <dave.nerd@gmail.com> - 0.09-1.fc
- Upgraded to 0.09.
- Changed Requires of clamtk to >= 3.00.

* Sat Jan 19 2008 Dave M. <dave.nerd@gmail.com> - 0.08-1.fc
- Upgraded to 0.08.
- Changed Requires line to kdelibs3.

* Sat Sep 8 2007 Dave M. <dave.nerd@gmail.com> - 0.07-1.fc
- Upgraded to 0.07.

* Tue Aug 7 2007 Dave M. <dave.nerd@gmail.com> - 0.06-1.fc
- Upgraded to 0.06.

* Mon Feb 12 2007 Dave M. <dave.nerd@gmail.com> - 0.05-1.fc
- Upgraded to 0.05.

* Sat Aug 12 2006 Dave M. <dave.nerd@gmail.com> - 0.04-1.fc
- Upgraded to 0.04.

* Mon Jul 3 2006 Dave M. <dave.nerd@gmail.com> - 0.03-1.fc
- Upgraded to 0.03.

* Thu Apr 27 2006 Dave M. <dave.nerd@gmail.com> - 0.02-1
- Upgraded to 0.02.
- Added man page.

* Fri Jan 20 2006 Dave M. <dave.nerd@gmail.com> - 0.01-1
- Initial release.
