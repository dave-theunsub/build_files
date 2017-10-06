Name: nemo-sendto-clamtk
Version: 0.04
Release: 1.fc
Summary: Simple extension to add virus scanning to nemo
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/dave_theunsub/nemo-sendto-clamtk/

Source: https://bitbucket.org/dave_theunsub/nemo-sendto-clamtk/downloads/nemo-sendto-clamtk-%{version}.tar.xz

BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: nemo, clamtk >= 5.00

%description
This is a simple extension to add context menu
virus scanning in the Nemo file manager.

ClamTk is a front-end for ClamAV Anti Virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/nemo/actions/ 
install -p -D -m0644 %{name}.nemo_action %{buildroot}/%{_datadir}/nemo/actions/ 
%files
%defattr(-, root, root, -)
%doc CHANGES DISCLAIMER LICENSE README.md
%{_datadir}/nemo/actions/%{name}.nemo_action

%changelog
* Fri Oct 6 2017 Dave M. <dave.nerd@gmail.com> - 0.04-1.fc
- Updated to release 0.04.
- Updated links.

* Mon Sep 5 2016 Dave M. <dave.nerd@gmail.com> - 0.03-1.fc
- Updated to release 0.03.
- Updated description and links.

* Sat Mar 15 2014 Dave M. <dave.nerd@gmail.com> - 0.02-1.fc
- Updated to release 0.02.

* Sat Nov 16 2013 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release 0.01.
