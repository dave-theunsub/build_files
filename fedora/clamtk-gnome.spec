Name: clamtk-gnome
Version: 6.15
Release: 1%{dist}
Summary: Adds context menu for virus scanning from within Gnome's file manager
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://github.com/dave-theunsub/clamtk-gnome

Source: https://github.com/dave-theunsub/clamtk-gnome/releases/download/v6.14/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: clamtk >= 6.00, nautilus-python >= 4

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
* Thu Dec 29 2022 Dave M. <dave.nerd@gmail.com> - 6.15-1
- Updated to release 6.15.
- Change nautilus-python requirement to >= 4

* Sat Nov 20 2021 Dave M. <dave.nerd@gmail.com> - 6.14-1
- Updated to release 6.14.
- Change version numbering.
- Implement dist tag.

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
