Name: clamtk
Version: 6.07
Release: 1.el8
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
Requires: clamav >= 0.95, clamav-update, clamav-data
Requires: cronie, adwaita-icon-theme

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
* Sun Jan 31 2021 Dave M. <dave.nerd@gmail.com> - 6.07-1%{dist}
- Updated to release 6.07.

* Wed Sep 16 2020 Dave M. <dave.nerd@gmail.com> - 6.06-1%{dist}
- Updated to release 6.06.
- Implement {dist} macro.

* Sun Aug 9 2020 Dave M. <dave.nerd@gmail.com> - 6.05-1.el8
- Updated to release 6.05.

* Thu Jul 23 2020 Dave M. <dave.nerd@gmail.com> - 6.04-1.el8
- Updated to release 6.04.

* Thu Apr 23 2020 Dave M. <dave.nerd@gmail.com> - 6.03-1.el8
- Updated to release 6.03.

* Fri Sep 27 2019 Dave M. <dave.nerd@gmail.com> - 6.02-1.el7
- Updated to release 6.02.

* Sun Mar 31 2019 Dave M. <dave.nerd@gmail.com> - 6.01-1.el7
- Updated to release 6.01.
- Updated Requires in spec.

* Fri Feb 22 2019 Dave M. <dave.nerd@gmail.com> - 6.00-1.el7
- Updated to release 6.00.
- Updated to use Gtk3.
