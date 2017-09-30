Name: thunar-sendto-clamtk
Version: 0.06
Release: 1.el7
Summary: Extension for Thunar to send files and directories for virus scanning
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/davem_/thunar-sendto-clamtk/

Source: https://bitbucket.org/davem_/thunar-sendto-clamtk/downloads/thunar-sendto-clamtk-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: Thunar, clamtk >= 5.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

ClamTk is a front-end for ClamAV Anti Virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

desktop-file-install --vendor "" \
	--dir $RPM_BUILD_ROOT%{_datadir}/Thunar/sendto \
	%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc CHANGES DISCLAIMER LICENSE README
%{_datadir}/Thunar/sendto/%{name}.desktop

%changelog
* Sat Sep 30 2017 Dave M. <dave.nerd@gmail.com> - 0.06-1.el7
- Update to 0.06.
- Update links.
- Update compression gz -> xz.

* Sat Mar 15 2014 Dave M. <dave.nerd@gmail.com> - 0.05-1.el6
- Update to 0.05.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 0.04-1.el6
- Update to 0.04.
- Updated Url and Source.
- Updated License field.

* Fri Apr 20 2012 Dave M. <dave.nerd@gmail.com> - 0.03-1.el6
- Update to 0.03.

* Fri Aug 12 2011 Dave M. <dave.nerd@gmail.com> - 0.02-1.el5
- Update to 0.02.

* Sat Jul 3 2010 Dave M. <dave.nerd@gmail.com> - 0.01-1.el5
- Initial release 0.01.
