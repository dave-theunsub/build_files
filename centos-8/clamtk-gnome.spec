Name: clamtk-gnome
Version: 0.05
Release: 1.el8
Summary: Adds context menu for virus scanning from within Gnome's file manager
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/davem_/clamtk-gnome/

Source: https://bitbucket.org/davem_/clamtk-gnome/downloads/%{name}-%{version}.tar.xz
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
* Sat Aug 15 2020 Dave M. <dave.nerd@gmail.com> - 0.05-1.el8
- Update to 0.05, using Gtk3. Requires perl-Gtk3.

* Sun Feb 9 2020 Dave M. <dave.nerd@gmail.com> - 0.04-1.el8
- First build for EPEL 8.

# End
