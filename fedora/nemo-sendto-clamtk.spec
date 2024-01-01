Name: nemo-sendto-clamtk
Version: 0.07
Release: 1%{dist}
Summary: Simple extension to add easy virus scanning option to nemo
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://github.com/dave-theunsub/nemo-sendto-clamtk

Source: https://github.com/dave-theunsub/clamtk/releases/download/%{version}/nemo-sendto-clamtk-%{version}.tar.xz

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
* Mon Jan 1 2024 Dave M. <dave.nerd@gmail.com> - 0.07-1
- Updated to release 0.07.

* Mon Feb 21 2022 Dave M. <dave.nerd@gmail.com> - 0.06-1
- Updated to release 0.06.

* Sat Apr 17 2021 Dave M. <dave.nerd@gmail.com> - 0.05-1
- Updated to release 0.05.
- Updated links.

* Fri Oct 6 2017 Dave M. <dave.nerd@gmail.com> - 0.04-1.fc
- Updated to release 0.04.
- Updated links.
- Updated compression from gz -> xz.

* Mon Sep 5 2016 Dave M. <dave.nerd@gmail.com> - 0.03-1.fc
- Updated to release 0.03.
- Updated description and links.

* Sat Mar 15 2014 Dave M. <dave.nerd@gmail.com> - 0.02-1.fc
- Updated to release 0.02.

* Sat Nov 16 2013 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release 0.01.
