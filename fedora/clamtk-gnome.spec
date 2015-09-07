Name: clamtk-gnome
Version: 0.01
Release: 1.fc
Summary: Adds context menu for virus scanning from within Gnome's file manager
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/dave_theunsub/clamtk-gnome/

Source: https://bitbucket.org/dave_theunsub/clamtk-gnome/downloads/%{name}-%{version}.tar.gz
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
# %{__install} -D -m0644 %{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files
%doc CHANGES DISCLAIMER LICENSE README

# Image
%{_datadir}/pixmaps/%{name}.png

# Man pages
%{_mandir}/man1/%{name}.1*

# Nautilus extension executable
%{_datadir}/nautilus-python/extensions/%{name}.py*

# Desktop file
# %{_datadir}/applications/%{name}.desktop

%changelog
* Sun Sep 6 2015 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release as a separate package
- Closes RH #1260284

# End
