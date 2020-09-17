Name: clamtk
Version: 6.06
Release: 1.el7
Summary: Easy to use graphical user interface for Clam Antivirus (ClamAV)
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/davem_/clamtk/

Source: https://bitbucket.org/davem_/clamtk/downloads/clamtk-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
Requires: perl(Gtk3)
Requires: perl(Text::CSV), perl(Time::Piece), perl(Locale::gettext), perl(JSON)
Requires: clamav >= 0.95, clamav-update, data(clamav)
Requires: gnome-icon-theme-legacy, cronie

%description
ClamTk is a front end for ClamAV anti-virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{perl_vendorlib}/ClamTk

install -p -D -m0755 clamtk %{buildroot}/%{_bindir}/clamtk
install -p -D -m0644 images/clamtk.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -p -D -m0644 clamtk.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
install -p -D -m0644 clamtk.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -p -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

# Install locale files
for n in po/*.mo ; do
	install -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

desktop-file-install --delete-original				\
	--dir=%{buildroot}/%{_datadir}/applications		\
	--add-category="GTK"					\
	--add-category="GNOME"					\
	--add-category="Utility"				\
	%{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc CHANGES DISCLAIMER LICENSE README.md credits.md

# The main executable
%{_bindir}/%{name}

# Main Perl libraries
%{perl_vendorlib}/ClamTk

# Images
%{_datadir}/pixmaps/%{name}.png

# Desktop file
%{_datadir}/applications/%{name}.desktop

# Man pages
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Sep 16 2020 Dave M. <dave.nerd@gmail.com> - 6.06-1%{dist}
- Updated to release 6.06.
- Implement {dist} macro.

* Sun Aug 9 2020 Dave M. <dave.nerd@gmail.com> - 6.05-1.el7
- Updated to release 6.05.

* Fri Sep 27 2019 Dave M. <dave.nerd@gmail.com> - 6.02-1.el7
- Updated to release 6.02.

* Sun Mar 31 2019 Dave M. <dave.nerd@gmail.com> - 6.01-1.el7
- Updated to release 6.01.
- Updated Requires in spec.

* Fri Feb 22 2019 Dave M. <dave.nerd@gmail.com> - 6.00-1.el7
- Updated to release 6.00.
- Updated to use Gtk3.

* Sat Feb 2 2019 Dave M. <dave.nerd@gmail.com> - 5.27-1.el7
- Updated to release 5.27.
- Removed obsolete scriptlets (post, postrun).

* Sat Aug 25 2018 Dave M. <dave.nerd@gmail.com> - 5.26-1.el7
- Updated to release 5.26.

* Mon Sep 4 2017 Dave M. <dave.nerd@gmail.com> - 5.25-1.el7
- Updated to release 5.25.
- Fix bitbucket URLs.
- Change compression from gz -> xz.

* Fri Nov 18 2016 Dave M. <dave.nerd@gmail.com> - 5.24-1.el7
- Updated to release 5.24.
- Remove help documentation.
- Rename README.md, add credits.md.

* Sat Oct 29 2016 Dave M. <dave.nerd@gmail.com> - 5.23-1.el7
- Updated to release 5.23.

* Sun Sep 18 2016 Dave M. <dave.nerd@gmail.com> - 5.22-1.el7
- Updated to release 5.22.

* Sun Aug 21 2016 Dave M. <dave.nerd@gmail.com> - 5.21-1.el7
- Updated to release 5.21.

* Sun Sep 6 2015 Dave M. <dave.nerd@gmail.com> - 5.20-1.el7
- Updated to release 5.20.
- Remove nautilus dependency.

* Sat Jun 27 2015 Dave M. <dave.nerd@gmail.com> - 5.19-1.el7
- Updated to release 5.19.

* Sun May 10 2015 Dave M. <dave.nerd@gmail.com> - 5.18-1.el7
- Updated to release 5.18.

* Sat Apr 11 2015 Dave M. <dave.nerd@gmail.com> - 5.17-1.el7
- Updated to release 5.17.

* Sat Apr 11 2015 Dave M. <dave.nerd@gmail.com> - 5.16-1.el7
- Updated to release 5.16.

* Thu Mar 5 2015 Dave M. <dave.nerd@gmail.com> - 5.15-1.el7
- Updated to release 5.15.

* Fri Feb 13 2015 Dave M. <dave.nerd@gmail.com> - 5.14-1.el7
- Updated to release 5.14.

* Sat Jan 3 2015 Dave M. <dave.nerd@gmail.com> - 5.13-1.el7
- Updated to release 5.13.

* Wed Dec 24 2014 Dave M. <dave.nerd@gmail.com> - 5.12-1.el7
- Updated to release 5.12.

* Fri Oct 31 2014 Dave M. <dave.nerd@gmail.com> - 5.11-1.el7
- Updated to release 5.11.

* Thu Oct 2 2014 Dave M. <dave.nerd@gmail.com> - 5.10-1.el7
- Updated to release 5.10.

* Fri Aug 29 2014 Dave M. <dave.nerd@gmail.com> - 5.09-1.el7
- Updated to release 5.09.

* Fri Aug 22 2014 Dave M. <dave.nerd@gmail.com> - 5.08-1.el7
- Updated to release 5.08.
- Initial CentOS 7 release.
