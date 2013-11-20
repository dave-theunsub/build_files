Name: nemo-sendto-clamtk
Version: 0.01
Release: 1.fc
Summary: Simple extension to add virus scanning to nemo
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: http://code.google.com/p/clamtk/

Source: https://bitbucket.org/dave_theunsub/nemo-sendto-clamtk/downloads/nemo-sendto-clamtk-%{version}.tar.gz

BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: nemo, clamtk >= 4.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

ClamTk is a front-end for ClamAV Anti Virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
# /usr/share/nemo/actions/
mkdir -p %{buildroot}/%{_datadir}/nemo/actions/ 
install -p -D -m0644 %{name}.nemo_action %{buildroot}/%{_datadir}/nemo/actions/ 
%files
%defattr(-, root, root, -)
%doc CHANGES DISCLAIMER LICENSE README
%{_datadir}/nemo/actions/%{name}.nemo_action

%changelog
* Sat Nov 16 2013 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release 0.01.
