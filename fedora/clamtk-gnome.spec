Name: clamtk-gnome
Version: 0.05
Release: 1.fc
Summary: Adds context menu for virus scanning from within Gnome's file manager
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/davem_/clamtk-gnome/

Source: https://bitbucket.org/davem_/clamtk-gnome/downloads/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: clamtk >= 5.20, nautilus-python

%description
clamtk-gnome adds right-click, context menu support for virus scanning
from within Gnome's file manager.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%{__install} -p -D -m0644 images/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%{__install} -p -D -m0644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
%{__install} -p -D -m0755 %{name}.py %{buildroot}/%{_datadir}/nautilus-python/extensions/%{name}.py

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files
%doc CHANGES DISCLAIMER LICENSE README.md

# Image
%{_datadir}/pixmaps/%{name}.png

# Man pages
%{_mandir}/man1/%{name}.1*

# Nautilus extension executable
%{_datadir}/nautilus-python/extensions/%{name}.py*

%changelog
* Sat Feb 22 2020 Dave M. <dave.nerd@gmail.com> - 0.05-1.fc
- Updated to release 0.05.

* Sun Feb 9 2020 Dave M. <dave.nerd@gmail.com> - 0.04-1.fc
- Updated to release 0.04.

* Sat Apr 13 2019 Dave M. <dave.nerd@gmail.com> - 0.03-1.fc
- New release allowing for python3.

* Thu Sep 7 2017 Dave M. <dave.nerd@gmail.com> - 0.02-1.fc
- Remove .desktop file.
- Update URLs.

* Sun Sep 6 2015 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release as a separate package
- Closes RH #1260284

# End
