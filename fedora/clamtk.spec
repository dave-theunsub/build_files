Name: clamtk
Version: 6.07
Release: 1%{dist}
Summary: Easy to use graphical user interface for Clam Antivirus (ClamAV)
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/davem_/clamtk/

Source: https://bitbucket.org/davem_/clamtk/downloads/clamtk-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Gtk3)
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
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
	--add-category="GTK"					\
	--add-category="GNOME"					\
	--add-category="Utility"				\
    --dir %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/applications/*

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
- Use {dist} macro.

* Sun Aug 9 2020 Dave M. <dave.nerd@gmail.com> - 6.05-1.fc
- Updated to release 6.05.

* Sat Jul 11 2020 Dave M. <dave.nerd@gmail.com> - 6.04-1.fc
- Updated to release 6.04.

* Thu Apr 23 2020 Dave M. <dave.nerd@gmail.com> - 6.03-1.fc
- Updated to release 6.03.

* Fri Sep 27 2019 Dave M. <dave.nerd@gmail.com> - 6.02-1.fc
- Updated to release 6.02.

* Sun Mar 31 2019 Dave M. <dave.nerd@gmail.com> - 6.01-1.fc
- Updated to release 6.01.
- Updated Requires in spec.

* Fri Feb 22 2019 Dave M. <dave.nerd@gmail.com> - 6.00-1.fc
- Updated to release 6.00.
- Updated to use Gtk3.

* Sat Feb 2 2019 Dave M. <dave.nerd@gmail.com> - 5.27-1.fc
- Updated to release 5.27.
- Removed obsolete scriptlets post, postrun

* Sat Aug 25 2018 Dave M. <dave.nerd@gmail.com> - 5.26-1.fc
- Updated to release 5.26.

* Mon Sep 4 2017 Dave M. <dave.nerd@gmail.com> - 5.25-1.fc
- Updated to release 5.25.
- Switched source from gz to xz.
- Updated bitbucket links.

* Fri Nov 18 2016 Dave M. <dave.nerd@gmail.com> - 5.24-1.fc
- Updated to release 5.24.
- Remove help docs
- Update other documentation names, add new credits.md

* Sat Oct 29 2016 Dave M. <dave.nerd@gmail.com> - 5.23-1.fc
- Updated to release 5.23.

* Sun Sep 18 2016 Dave M. <dave.nerd@gmail.com> - 5.22-1.fc
- Updated to release 5.22.

* Sun Aug 21 2016 Dave M. <dave.nerd@gmail.com> - 5.21-1.fc
- Updated to release 5.21.

* Sat Sep 5 2015 Dave M. <dave.nerd@gmail.com> - 5.20-1.fc
- Updated to release 5.20.
- Removed nautilus dependency.

* Fri Jun 26 2015 Dave M. <dave.nerd@gmail.com> - 5.19-1.fc
- Updated to release 5.19.

* Sun May 10 2015 Dave M. <dave.nerd@gmail.com> - 5.18-1.fc
- Updated to release 5.18.

* Sat Apr 11 2015 Dave M. <dave.nerd@gmail.com> - 5.17-1.fc
- Updated to release 5.17.

* Sat Apr 11 2015 Dave M. <dave.nerd@gmail.com> - 5.16-1.fc
- Updated to release 5.16.

* Thu Mar 5 2015 Dave M. <dave.nerd@gmail.com> - 5.15-1.fc
- Updated to release 5.15.

* Fri Feb 13 2015 Dave M. <dave.nerd@gmail.com> - 5.14-1.fc
- Updated to release 5.14.

* Sat Jan 3 2015 Dave M. <dave.nerd@gmail.com> - 5.13-1.fc
- Updated to release 5.13.

* Wed Dec 24 2014 Dave M. <dave.nerd@gmail.com> - 5.12-1.fc
- Updated to release 5.12.

* Fri Oct 31 2014 Dave M. <dave.nerd@gmail.com> - 5.11-1.fc
- Updated to release 5.11.

* Thu Oct 2 2014 Dave M. <dave.nerd@gmail.com> - 5.10-1.fc
- Updated to release 5.10.

* Fri Aug 29 2014 Dave M. <dave.nerd@gmail.com> - 5.09-1.fc
- Updated to release 5.09.

* Sun Aug 24 2014 Dave M. <dave.nerd@gmail.com> - 5.08-1.fc
- Updated to release 5.08.

* Thu Jun 12 2014 Dave M. <dave.nerd@gmail.com> - 5.07-1.fc
- Updated to release 5.07.

* Sat May 3 2014 Dave M. <dave.nerd@gmail.com> - 5.06-1.fc
- Updated to release 5.06.
- Remove zenity dependency from spec.

* Fri Mar 14 2014 Dave M. <dave.nerd@gmail.com> - 5.05-1.fc
- Updated to release 5.05.

* Tue Feb 11 2014 Dave M. <dave.nerd@gmail.com> - 5.04-1.fc
- Updated to release 5.04.

* Sun Jan 19 2014 Dave M. <dave.nerd@gmail.com> - 5.03-1.fc
- Updated to release 5.03.
- Adding gnome-icon-theme-legacy as dependency.
- Add cronie dependency back.

* Sat Dec 21 2013 Dave M. <dave.nerd@gmail.com> - 5.02-1.fc
- Updated to release 5.02.

* Thu Nov 21 2013 Dave M. <dave.nerd@gmail.com> - 5.01-1.fc
- Updated to release 5.01.
- Requirement for perl-Gtk2 upped to >= 1.241.
- Minor spec cleanup.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 5.00-1.fc
- Updated to release 5.00.
- Added help files.
- Added nautilus-python and perl-LWP-Protocol-https to dependencies.
- Updated Url and Source.
- Updated License field to Artistic 2.0.

* Wed Sep 04 2013 Dave M. <dave.nerd@gmail.com> - 4.46-1.fc
- Updated to release 4.46.

* Wed May 22 2013 Dave M. <dave.nerd@gmail.com> - 4.45-1.fc
- Updated to release 4.45.

* Sat Dec 22 2012 Dave M. <dave.nerd@gmail.com> - 4.44-1.fc
- Updated to release 4.44.

* Sun Dec 2 2012 Dave M. <dave.nerd@gmail.com> - 4.43-1.fc
- Updated to release 4.43.

* Wed Sep 12 2012 Dave M. <dave.nerd@gmail.com> - 4.42-1.fc
- Updated to release 4.42.

* Fri Jun 1 2012 Dave M. <dave.nerd@gmail.com> - 4.41-1.fc
- Updated to release 4.41.

* Fri May 25 2012 Dave M. <dave.nerd@gmail.com> - 4.40-1.fc
- Updated to release 4.40.
- Images are grouped under images/ now.

* Fri Apr 20 2012 Dave M. <dave.nerd@gmail.com> - 4.39-1.fc
- Updated to release 4.39.

* Sat Mar 24 2012 Dave M. <dave.nerd@gmail.com> - 4.38-1.fc
- Updated to release 4.38.

* Fri Feb 3 2012 Dave M. <dave.nerd@gmail.com> - 4.37-1.fc
- Updated to release 4.37.

* Sat Oct 15 2011 Dave M. <dave.nerd@gmail.com> - 4.36-1.fc
- Updated to release 4.36.

* Thu Sep 8 2011 Dave M. <dave.nerd@gmail.com> - 4.35-1.fc
- Updated to release 4.35.

* Fri Aug 12 2011 Dave M. <dave.nerd@gmail.com> - 4.34-1.fc
- Updated to release 4.34.

* Sat Jun 11 2011 Dave M. <dave.nerd@gmail.com> - 4.33-1.fc
- Updated to release 4.33.

* Sun Apr 24 2011 Dave M. <dave.nerd@gmail.com> - 4.32-1.fc
- Updated to release 4.32.

* Sat Jan 8 2011 Dave M. <dave.nerd@gmail.com> - 4.31-1.fc
- Updated to release 4.31.
- Dependency clamav-data changed to data(clamav).

* Sat Nov 6 2010 Dave M. <dave.nerd@gmail.com> - 4.30-1.fc
- Updated to release 4.30.

* Fri Sep 10 2010 Dave M. <dave.nerd@gmail.com> - 4.29-1.fc
- Updated to release 4.29.
- ClamAV dependency is bumped to >= 0.95.

* Tue Aug 17 2010 Dave M. <dave.nerd@gmail.com> - 4.28-1.fc
- Updated to release 4.28.
- Removed dependency on hal (deprecated).
- Added dependency on udev.

* Fri Jul 9 2010 Dave M. <dave.nerd@gmail.com> - 4.27-1.fc
- Updated to release 4.27.
- Added dependency on hal.

* Fri Apr 30 2010 Dave M. <dave.nerd@gmail.com> - 4.26-1.fc
- Updated to release 4.26.

* Fri Mar 5 2010 Dave M. <dave.nerd@gmail.com> - 4.25-1.fc
- Updated to release 4.25.

* Sat Feb 27 2010 Dave M. <dave.nerd@gmail.com> - 4.24-1.fc
- Updated to release 4.24.
- Spelling of Antivirus changed to anti virus to accomodate rpmlint.
  (mood: irritated).

* Sun Jan 17 2010 Dave M. <dave.nerd@gmail.com> - 4.23-1.fc
- Updated to release 4.23.
- Removed perl(gettext) from Requires.
- Replaced perl(libwww-perl) with perl(LWP::UserAgent).

* Wed Dec 23 2009 Dave M. <dave.nerd@gmail.com> - 4.22-1.fc
- Updated to release 4.22.
- License updated as GPL+ or Artistic.
- desktop-file-utils is now BuildRequires.

* Fri Dec 4 2009 Dave M. <dave.nerd@gmail.com> - 4.21-1.fc
- Updated to release 4.21.
- Changed category from GNOME to Security.
- install is now install -p

* Sat Oct 31 2009 Dave M. <dave.nerd@gmail.com> - 4.20-1.fc
- Updated to release 4.20.
- Corrected dependency from crontabs to cronie.
- Added versioned MODULE_COMPAT_Requires for Perl.
- Reformatted rpm spec file.

* Tue Oct 6 2009 Dave M. <dave.nerd@gmail.com> - 4.19-1.fc
- Updated to release 4.19.
- Added Bulgarian (bg) language support.

* Sat Sep 19 2009 Dave M. <dave.nerd@gmail.com> - 4.18-1.fc
- Updated to release 4.18.
- Added crontabs requirement.
- Removed requirement perl-Config-Tiny.
- Changed library path to be more compliant.
- Added Hungarian (hu) language.
- Added Norwegian Bokmal (nb) language.

* Sat Aug 8 2009 Dave M. <dave.nerd@gmail.com> - 4.17-1.fc
- Updated to release 4.17.

* Sat Jul 11 2009 Dave M. <dave.nerd@gmail.com> - 4.16-1.fc
- Updated to release 4.16.
- Added Malay (ms) language.
- Added English (en_GB) language.
- Added Norwegian Nynorsk (nn) language.
- Added Croatian (hr) language.

* Sat Jun 20 2009 Dave M. <dave.nerd@gmail.com> - 4.15-1.fc
- Updated to release 4.15.
- Added Arabic language.

* Sat Jun 13 2009 Dave M. <dave.nerd@gmail.com> - 4.14-1.fc
- Updated to release 4.14.

* Sat May 23 2009 Dave M. <dave.nerd@gmail.com> - 4.13-1.fc
- Updated to release 4.13.
- Added Dutch language.
- Added Greek language.
- Updated RPM group.

* Sat Apr 25 2009 Dave M. <dave.nerd@gmail.com> - 4.12-1.fc
- Updated to release 4.12.
- Added Turkish (tr) language.
- Added perl-Net-DNS requirement.
- Removed bind-utils requirement.

* Sun Mar 22 2009 Dave M. <dave.nerd@gmail.com> - 4.11-1.fc
- Updated to release 4.11.
- Added Slovak (sk) language.

* Tue Feb 17 2009 Dave M. <dave.nerd@gmail.com> - 4.10-1.fc
- Updated to release 4.10.

* Fri Feb 13 2009 Dave M. <dave.nerd@gmail.com> - 4.09-1.fc
- Updated to release 4.09.

* Sat Dec 27 2008 Dave M. <dave.nerd@gmail.com> - 4.08-1.fc
- Updated to release 4.08.

* Wed Dec 17 2008 Dave M. <dave.nerd@gmail.com> - 4.07-1.fc
- Updated to release 4.07.

* Sun Dec 7 2008 Dave M. <dave.nerd@gmail.com> - 4.06-1.fc
- Updated to release 4.06.
- Added requirement bind-utils.

* Thu Nov 27 2008 Dave M. <dave.nerd@gmail.com> - 4.05-1.fc
- Updated to release 4.05.

* Sun Nov 16 2008 Dave M. <dave.nerd@gmail.com> - 4.04-1.fc
- Updated to release 4.04.

* Sat Nov 8 2008 Dave M. <dave.nerd@gmail.com> - 4.03-1.fc
- Updated to release 4.03.
- Removed clamav-lib from Requires field as it is not necessary.

* Sun Oct 26 2008 Dave M. <dave.nerd@gmail.com> - 4.02-1.fc
- Updated to release 4.02.

* Sat Oct 18 2008 Dave M. <dave.nerd@gmail.com> - 4.01-1.fc
- Updated to release 4.01.
- Added the missing zenity requirement.

* Sun Oct 12 2008 Dave M. <dave.nerd@gmail.com> - 4.00-1.fc
- Updated to release 4.00.
- Added perl-libwww-perl dependency.
- Added directory for .pm files.
- License is now Artistic 2.0.

* Wed Aug 27 2008 Dave M. <dave.nerd@gmail.com> - 3.11-1.fc
- Updated to release 3.11.
- Added Japanese (ja_JP) language file.

* Sat Jun 14 2008 Dave M. <dave.nerd@gmail.com> - 3.10-1.fc
- Updated to release 3.10.
- Added Dutch (nl) language file.

* Sun May 25 2008 Dave M. <dave.nerd@gmail.com> - 3.09-1.fc
- Updated to release 3.09.

* Tue Feb 5 2008 Dave M. <dave.nerd@gmail.com> - 3.08-1.fc
- Updated to release 3.08.
- Added Korean (ko_KR) language support.
- Added Romanian (ro_RO) language support.

* Sat Jan 19 2008 Dave M. <dave.nerd@gmail.com> - 3.07-1.fc
- Updated to release 3.07.
- Changed minimum clamav to 0.90.
- Added dependency perl-Config-Tiny.
- Added Slovene (sl) language support.

* Sun Dec 30 2007 Dave M. <dave.nerd@gmail.com> - 3.06-1.fc
- Updated to release 3.06.

* Thu Dec 13 2007 Dave M. <dave.nerd@gmail.com> - 3.05-1.fc
- Updated to release 3.05.

* Sun Sep 16 2007 Dave M. <dave.nerd@gmail.com> - 3.04-1.fc
- Updated to release 3.04.

* Wed Sep 12 2007 Dave M. <dave.nerd@gmail.com> - 3.03-1.fc
- Updated to release 3.03.

* Sat Sep 08 2007 Dave M. <dave.nerd@gmail.com> - 3.02-1.fc
- Updated to release 3.02.
- Language file for Galician added.

* Thu Aug 30 2007 Dave M. <dave.nerd@gmail.com> - 3.01-1.fc
- Updated to release 3.01.

* Tue Aug 07 2007 Dave M. <dave.nerd@gmail.com> - 3.00-1.fc
- Updated to release 3.00.
- Language file for Swedish added.

* Sun Jun 24 2007 Dave M. <dave.nerd@gmail.com> - 2.99-1.fc
- Updated to release 2.99.
- perl-Gtk2 requirement is now 1.140.

* Sun May 13 2007 Dave M. <dave.nerd@gmail.com> - 2.32-1.fc
- Updated to release 2.32.

* Sat Mar 10 2007 Dave M. <dave.nerd@gmail.com> - 2.31-1.fc
- Updated to release 2.31.

* Fri Mar 09 2007 Dave M. <dave.nerd@gmail.com> - 2.30-1.fc
- Updated to release 2.30.

* Sun Mar 04 2007 Dave M. <dave.nerd@gmail.com> - 2.29-1.fc
- Updated to release 2.29.

* Mon Feb 12 2007 Dave M. <dave.nerd@gmail.com> - 2.28-1.fc
- Updated to release 2.28.
- Added support for Czech (cs_CZ).

* Wed Jan 10 2007 Dave M. <dave.nerd@gmail.com> - 2.27-1.fc
- Updated to release 2.27.
- Replaced clam.xpm with clamtk.png.

* Sat Oct 28 2006 Dave M. <dave.nerd@gmail.com> - 2.26-1.fc
- Updated to release 2.26.

* Wed Oct 18 2006 Dave M. <dave.nerd@gmail.com> - 2.25-1.fc
- Updated to release 2.25.

* Sat Sep 23 2006 Dave M. <dave.nerd@gmail.com> - 2.24-1.fc
- Updated to release 2.24.
- Added Spanish and Polish language support.

* Sat Aug 12 2006 Dave M. <dave.nerd@gmail.com> - 2.23-1.fc
- Updated to release 2.23.

* Sat Jul 29 2006 Dave M. <dave.nerd@gmail.com> - 2.22-1.fc
- Added Russian language support.

* Tue Jul 4 2006 Dave M. <dave.nerd@gmail.com> - 2.21-1.fc
- Added French and Italian support.
- Updated to release 2.21.

* Wed Jun 14 2006 Dave M. <dave.nerd@gmail.com> - 2.20-1.fc
- Added locale lines.
- Added perl-gettext/perl-Locale-gettext as a requirement under Requires.
- Removed clamtk.xml.
- Updated to release 2.20.

* Mon May 15 2006 Dave M. <dave.nerd@gmail.com> - 2.19-1
- Updated to release 2.19.

* Sat May 6 2006 Dave M. <dave.nerd@gmail.com> - 2.18-1
- Updated to release 2.18.
- Removed hard-coded packager line.

* Sat Apr 22 2006 Dave M. <dave.nerd@gmail.com> - 2.17-1
- Updated to release 2.17.
- clamav rpm version changed back to >= 83.
- perl-Gtk2 rpm version changed back to >= 1.102.

* Sun Mar 19 2006 Dave M. <dave.nerd@gmail.com> - 2.16-1
- Updated to release 2.16.
- Added requirement of perl-Gtk2 >= 1.120.

* Sun Feb 12 2006 Dave M. <dave.nerd@gmail.com> - 2.15-1
- Updated to release 2.15.
- Added man page.
- Added BuildArch: noarch.

* Mon Jan 16 2006 Dave M. <dave.nerd@gmail.com> - 2.14-1
- Updated to release 2.14.
- Removed manual creation of .desktop file.
- Added clamtk.desktop and clamtk.xml.

* Sun Jan 1 2006 Dave M. <dave.nerd@gmail.com> - 2.13-1
- Updated to release 2.13.

* Fri Dec 23 2005 Dave M. <dave.nerd@gmail.com> - 2.12-1
- Updated to release 2.12.
- Updated dependencies by removing perl-libwww-perl.

* Sat Dec 10 2005 Dave M. <dave.nerd@gmail.com> - 2.11-1
- Updated to release 2.11.

* Sun Nov 27 2005 Dave M. <dave.nerd@gmail.com> - 2.10-1
- Updated to release 2.10.

* Sat Nov 26 2005 Dave M. <dave.nerd@gmail.com> - 2.09-1
- Updated to release 2.09.

* Fri Nov 11 2005 Dave M. <dave.nerd@gmail.com> - 2.08-1
- Updated to release 2.08.
- Updated dependencies.

* Sat Oct 22 2005 Dave M. <dave.nerd@gmail.com> - 2.07-1
- Updated to release 2.07.

* Sun Aug 28 2005 Dave M. <dave.nerd@gmail.com> - 2.06-1
- Updated to release 2.06.

* Sat Aug 20 2005 Dave M. <dave.nerd@gmail.com> - 2.05-1
- Updated to release 2.05.
- Changed license from Perl to Artistic.

* Sun Jul 17 2005 Dave M. <dave.nerd@gmail.com> - 2.04-1
- Updated to release 2.04.

* Sat Jul 09 2005 Dave M. <dave.nerd@gmail.com> - 2.03-1
- Updated to release 2.03.

* Sat Jul 02 2005 Dave M. <dave.nerd@gmail.com> - 2.02-1
- Updated to release 2.02.

* Sat Jun 25 2005 Dave M. <dave.nerd@gmail.com> - 2.01-1
- Changed dependencies to fit Fedora Extras different naming scheme.
- Updated to release 2.01.

* Sat Jun 11 2005 Dave M. <dave.nerd@gmail.com> - 2.00-1
- Updated to release 2.00.

* Wed May 18 2005 Dave M. <dave.nerd@gmail.com> - 1.99-1
- Updated to release 1.99.

* Sun May 08 2005 Dave M. <dave.nerd@gmail.com> - 1.98-1
- Updated to release 1.98.

* Thu May 05 2005 Dag Wieers <dag@wieers.com> - 1.97-1 - 3063+/dag
- Updated to release 1.97.
- Added changes from Dave M.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Initial package. (using DAR)
