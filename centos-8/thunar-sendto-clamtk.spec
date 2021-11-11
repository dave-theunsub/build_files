Name: thunar-sendto-clamtk
Version: 0.07
Release: 1%{dist}
Summary: Extension for Thunar to send files and directories for virus scanning
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://github.com/dave-theunsub/thunar-sendto-clamtk

Source: https://github.com/dave-theunsub/thunar-sendto-clamtk/releases/download/v%{version}/thunar-sendto-clamtk-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: Thunar, clamtk >= 5.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

With this extension installed, it is easy to scan files for threats.

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
%doc CHANGES DISCLAIMER LICENSE README.md
%{_datadir}/Thunar/sendto/%{name}.desktop

%changelog
* Sun Nov 7 2021 Dave M. <dave.nerd@gmail.com> - 0.07-1
- Update to 0.07.
- Update links.
- Remove .fc tags.

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
