Name: clamtk-gnome
Version: 6.14
Release: 1%{dist}
Summary: Adds context menu for virus scanning from within Gnome's file manager
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://github.com/dave-theunsub/clamtk-gnome

Source: https://github.com/dave-theunsub/clamtk-gnome/releases/download/v6.14/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: clamtk >= 5.20, nautilus-python, perl-Gtk3

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
* Sat Nov 20 2021 Dave M. <dave.nerd@gmail.com> - 6.14-1
- Update to 6.14.
- Change in version numbering.
- Implement dist tag.

* Sat Aug 15 2020 Dave M. <dave.nerd@gmail.com> - 0.05-1.el8
- Update to 0.05, using Gtk3. Requires perl-Gtk3.

* Sun Feb 9 2020 Dave M. <dave.nerd@gmail.com> - 0.04-1.el8
- First build for EPEL 8.

# End
