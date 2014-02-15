Name: clamtk
Version: 5.04
Release: 1.el6
Summary: Easy to use front-end for ClamAV
License: GPL+ or Artistic 2.0
Group: Applications/File
URL: http://code.google.com/p/clamtk/

Source: https://bitbucket.org/dave_theunsub/clamtk/downloads/clamtk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: clamav >= 0.95, clamav-db
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
Requires: perl(IO::Socket::SSL)
Requires: zenity, gnome-icon-theme, cronie
Requires: perl(Gtk2) >= 1.248
# This doesn't work on CentOS.
# Requires: nautilus-python

%description
ClamTk is a front-end for ClamAV anti virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}/
install -p -D -m0755 clamtk %{buildroot}/%{_bindir}/clamtk
# This doesn't work on CentOS.
# install -p -D -m0755 clamtk.py %{buildroot}/%{_datadir}/nautilus-python/extensions/clamtk.py
install -p -D -m0644 images/clamtk.png %{buildroot}/%{_datadir}/pixmaps/clamtk.png
install -p -D -m0644 clamtk.1.gz %{buildroot}/%{_mandir}/man1/clamtk.1.gz
install -p -D -m0644 clamtk.desktop %{buildroot}/%{_datadir}/applications/clamtk.desktop
install -p -d %{buildroot}/%{perl_vendorlib}/ClamTk
install -p -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

# Install help files
# CentOS uses /usr/share/gnome/help/$package/$locale,
# while our package is clamtk-X-XX/help/$locale/$package.
# Thanks for making that easy.
mkdir -p %{buildroot}/%{_datadir}/gnome/help/%{name}
for dir in help/* ; do
	basename=`basename $dir`
	mkdir -p %{buildroot}/%{_datadir}/gnome/help/%{name}/$basename
	cp -a help/$basename/%{name}/* %{buildroot}/%{_datadir}/gnome/help/%{name}/$basename/
done

# Install locale files
for n in po/*.mo ; do
	%{__install} -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

desktop-file-install --vendor misc				\
	--dir %{buildroot}/%{_datadir}/applications		\
	--delete-original				 	\
	--add-category="GTK"					\
	--add-category="GNOME"				\
	--add-category="Utility"				\
	%{buildroot}/%{_datadir}/applications/*.desktop
	
%find_lang %{name} --with-gnome

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, -)
%doc CHANGES DISCLAIMER LICENSE README
# The main executable
%{_bindir}/%{name}

# This doesn't work on CentOS.
# Nautilus python extension executable
# %{_datadir}/nautilus-python/extensions/%{name}.py*

# Main Perl libraries
%{perl_vendorlib}/ClamTk

# Images
%{_datadir}/pixmaps/%{name}.png

# Desktop file
%{_datadir}/applications/*.desktop

# Help files
#%{_datadir}/gnome/help/%{name}/

# Man pages
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Feb 11 2014 Dave M. <dave.nerd@gmail.com> - 5.04-1.el6
- Updated to release 5.04.

* Sun Jan 19 2014 Dave M. <dave.nerd@gmail.com> - 5.03-1.el6
- Updated to release 5.03.
- Added gnome-icon-theme as dependency.
- Add cronie dependency back.

* Sat Dec 21 2013 Dave M. <dave.nerd@gmail.com> - 5.02-1.el6
- Updated to release 5.02.

* Thu Nov 21 2013 Dave M. <dave.nerd@gmail.com> - 5.01-1.el6
- Updated to release 5.01.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 5.00-1.el6
- Updated to release 5.00.
- Updated requirements.
- Updated Url and Source.
- Updated License field.

* Fri May 24 2013 Dave M. <dave.nerd@gmail.com> - 4.45-1.el6
- Updated to release 4.45.

* Sat Dec 22 2012 Dave M. <dave.nerd@gmail.com> - 4.44-1.el6
- Updated to release 4.44.

* Sun Dec 2 2012 Dave M. <dave.nerd@gmail.com> - 4.43-1.el6
- Updated to release 4.43.

* Wed Sep 12 2012 Dave M. <dave.nerd@gmail.com> - 4.42-1.el6
- Updated to release 4.42.

* Fri Jun 1 2012 Dave M. <dave.nerd@gmail.com> - 4.41-1.el6
- Updated to release 4.41.

* Fri May 25 2012 Dave M. <dave.nerd@gmail.com> - 4.40-1.el6
- Updated to release 4.40.
- Images are grouped under images/ now.

* Sat Apr 21 2012 Dave M. <dave.nerd@gmail.com> - 4.39-1.el6
- Updated to release 4.39.

* Sat Mar 24 2012 Dave M. <dave.nerd@gmail.com> - 4.38-1.el6
- Updated to release 4.38.

* Fri Feb 3 2012 Dave M. <dave.nerd@gmail.com> - 4.37-1.el6
- Updated to release 4.37.

* Sat Oct 15 2011 Dave M. <dave.nerd@gmail.com> - 4.36-1.el6
- Updated to release 4.36.

* Thu Sep 8 2011 Dave M. <dave.nerd@gmail.com> - 4.35-1.el6
- Updated to release 4.35.

* Fri Aug 19 2011 Dave M. <dave.nerd@gmail.com> - 4.34-1.el6
- Initial release for CentOS 6.0.

* Fri Aug 12 2011 Dave M. <dave.nerd@gmail.com> - 4.34-1.el5
- Updated to release 4.34.

* Sat Jun 11 2011 Dave M. <dave.nerd@gmail.com> - 4.33-1.el5
- Updated to release 4.33.

* Sun Apr 24 2011 Dave M. <dave.nerd@gmail.com> - 4.32-1.el5
- Updated to release 4.32.

* Sat Jan 8 2011 Dave M. <dave.nerd@gmail.com> - 4.31-1.el5
- Updated to release 4.31.

* Sat Nov 6 2010 Dave M. <dave.nerd@gmail.com> - 4.30-1.el5
- Updated to release 4.30.

* Fri Sep 10 2010 Dave M. <dave.nerd@gmail.com> - 4.29-1.el5
- Updated to release 4.29.
- ClamAV dependency is now >= 0.95.

* Sun Aug 15 2010 Dave M. <dave.nerd@gmail.com> - 4.28-1.el5
- Updated to release 4.28.
- Removed dependency for hal.
- Added dependency for udev.

* Fri Jul 9 2010 Dave M. <dave.nerd@gmail.com> - 4.27-1.el5
- Updated to release 4.27.
- Added dependency for hal.
- Built to rpmforge clamav dependencies again (removed clamav-update).

* Tue Apr 27 2010 Dave M. <dave.nerd@gmail.com> - 4.26-1.el5
- Updated to release 4.26.

* Fri Mar 5 2010 Dave M. <dave.nerd@gmail.com> - 4.25-1.el5
- Updated to release 4.25.

* Sat Feb 27 2010 Dave M. <dave.nerd@gmail.com> - 4.24-1.el5
- Updated to release 4.24.

* Fri Jan 8 2010 Dave M. <dave.nerd@gmail.com> - 4.23-1.el5
- Updated to release 4.23.
- Requires perl(libwww-perl) updated to perl(LWP::UserAgent).

* Wed Dec 23 2009 Dave M. <dave.nerd@gmail.com> - 4.22-1.el5
- Updated to release 4.22.
- License updated as GPL+ or Artistic.
- desktop-file-utils is now BuildRequires.

* Sun Nov 28 2009 Dave M. <dave.nerd@gmail.com> - 4.21-1.el5
- Updated to release 4.21.
- install is now install -p.

* Sat Oct 31 2009 Dave M. <dave.nerd@gmail.com> - 4.20-1.el5
- Updated to release 4.20.
- Reformatted rpm spec file.

* Tue Oct 6 2009 Dave M. <dave.nerd@gmail.com> - 4.19-1.el5
- Updated to release 4.19.
- Added Bulgarian (bg) language support.
- Removed obsoletes line (clamtk-kde).

* Sat Sep 19 2009 Dave M. <dave.nerd@gmail.com> - 4.18-1.el5
- Updated to release 4.18.
- Added vixie-cron requirement.
- Removed perl-Config-Tiny.
- Changed library path to be more compliant.
- Added Hungarian (hu) language.
- Added Norwegian Bokmal (nb) language.

* Sat Aug 8 2009 Dave M. <dave.nerd@gmail.com> - 4.17-1.el5
- Updated to release 4.17.

* Sat Jul 11 2009 Dave M. <dave.nerd@gmail.com> - 4.16-1.el5
- Updated to release 4.16.
- Added Malay (ms) language support.
- Added English (en_GB) language support.
- Added Norwegian Nynorsk (nn) language support.
- Added Croatian (hr) language support.


* Sat Jun 20 2009 Dave M. <dave.nerd@gmail.com> - 4.15-1.el5
- Updated to release 4.15.
- Added Arabic language support.

* Sat Jun 13 2009 Dave M. <dave.nerd@gmail.com> - 4.14-1.el5
- Updated to release 4.14.

* Sat May 23 2009 Dave M. <dave.nerd@gmail.com> - 4.13-1.el5
- Updated to release 4.13.
- Added Dutch language support.
- Added Greek language support.
- Obsoletes clamtk-kde line added.

* Sat Apr 25 2009 Dave M. <dave.nerd@gmail.com> - 4.12-1.el5
- Updated to release 4.12.
- Added Turkish language support.
- Added clamav-update as a dependency for freshclam command.
- Removed the bind-utils requirement.
- Added perl-Net-DNS requirement.

* Sun Mar 22 2009 Dave M. <dave.nerd@gmail.com> - 4.11-1.el5
- Updated to release 4.11.
- Added Slovak (sk) language file.

* Tue Feb 17 2009 Dave M. <dave.nerd@gmail.com> - 4.10-1.el5
- Updated to release 4.10.

* Fri Feb 13 2009 Dave M. <dave.nerd@gmail.com> - 4.09-1.el5
- Updated to release 4.09.

* Sat Dec 27 2008 Dave M. <dave.nerd@gmail.com> - 4.08-1.el5
- Updated to release 4.08.

* Sat Dec 20 2008 Dave M. <dave.nerd@gmail.com> - 4.07-1.el5
- Updated to release 4.07.

* Sun Dec 7 2008 Dave M. <dave.nerd@gmail.com> - 4.06-1.el5
- Updated to release 4.06.
- Added requirement bind-utils.

* Thu Nov 27 2008 Dave M. <dave.nerd@gmail.com> - 4.05-1.el5
- Updated to release 4.05.

* Sun Nov 16 2008 Dave M. <dave.nerd@gmail.com> - 4.04-1.el5
- Updated to release 4.04.

* Sat Nov 8 2008 Dave M. <dave.nerd@gmail.com> - 4.03-1.el5
- Updated to release 4.03.

* Sun Oct 26 2008 Dave M. <dave.nerd@gmail.com> - 4.02-1.el5
- Updated to release 4.02.

* Sat Oct 18 2008 Dave M. <dave.nerd@gmail.com> - 4.01-1.el5
- Updated to release 4.01.
- Added the missing zenity requirement.

* Sun Oct 12 2008 Dave M. <dave.nerd@gmail.com> - 4.00-1.el5
- Updated to release 4.00.
- Added perl-libwww-perl requirement.
- Added directory for *.pm files.

* Wed Aug 27 2008 Dave M. <dave.nerd@gmail.com> - 3.11-1.el5
- Updated to release 3.11.
- Added Japanese (ja_JP) language support.

* Sat Jun 14 2008 Dave M. <dave.nerd@gmail.com> - 3.10-1.el5
- Updated to release 3.10.
- Added Dutch (nl) language support.
- Added Slovene support (sl) - for real this time.

* Sun May 25 2008 Dave M. <dave.nerd@gmail.com> - 3.09-1.el5
- Updated to release 3.09.

* Tue Feb 5 2008 Dave M. <dave.nerd@gmail.com> - 3.08-1.el5
- Updated to release 3.08.
- Added Korean language support (ko_KR).
- Added Romanian language support (ro_RO).

* Sat Jan 19 2008 Dave M. <dave.nerd@gmail.com> - 3.07-1.el5
- Updated to release 3.07.
- Added requirement perl-Config-Tiny.
- Added Slovene support (sl_SI).
- Updated minimum clamav requirement to >= 0.90.

* Sun Dec 30 2007 Dave M. <dave.nerd@gmail.com> - 3.06-1.el5
- Updated to release 3.06.

* Thu Dec 13 2007 Dave M. <dave.nerd@gmail.com> - 3.05-1.el5
- Updated to release 3.05.

* Sun Sep 16 2007 Dave M. <dave.nerd@gmail.com> - 3.04-1.el5
- Updated to release 3.04.

* Wed Sep 12 2007 Dave M. <dave.nerd@gmail.com> - 3.03-1.el5
- Updated to release 3.03.

* Sat Sep 08 2007 Dave M. <dave.nerd@gmail.com> - 3.02-1.centos
- Updated to release 3.02.
- Added Galician language. 

* Thu Aug 30 2007 Dave M. <dave.nerd@gmail.com> - 3.01-1.centos
- Updated to release 3.01.
- Added Swedish language - should have been in 3.00.

* Mon Aug 6 2007 Dave M. <dave.nerd@gmail.com> - 3.00-1.centos
- Updated to release 3.00.

* Sun Jun 24 2007 Dave M. <dave.nerd@gmail.com> - 2.99-1.centos
- Updated to release 2.99.
- Increased perl-Gtk2 requirement to >= 1.140.

* Sun May 13 2007 Dave M. <dave.nerd@gmail.com> - 2.32-1.centos
- Updated to release 2.32.

* Sat Mar 10 2007 Dave M. <dave.nerd@gmail.com> - 2.31-1.centos
- Updated to release 2.31.

* Fri Mar 09 2007 Dave M. <dave.nerd@gmail.com> - 2.30-1.centos
- Updated to release 2.30.

* Sun Mar 04 2007 Dave M. <dave.nerd@gmail.com> - 2.29-1.centos
- Updated to release 2.29.

* Mon Feb 12 2007 Dave M. <dave.nerd@gmail.com> - 2.28-1.centos
- Updated to release 2.28.
- Added additional language support (cs_CZ).

* Wed Jan 10 2007 Dave M. <dave.nerd@gmail.com> - 2.27-1.centos
- Updated to release 2.27.
- Replaced clam.xpm with clamtk.png.

* Sat Oct 28 2006 Dave M. <dave.nerd@gmail.com> - 2.26-1.centos
- Updated to release 2.26.

* Sat Sep 23 2006 Dave M. <dave.nerd@gmail.com> - 2.24-1.centos
- Updated to release 2.24.
- Updated for Centos 4.4.

* Sat Aug 12 2006 Dave M. <dave.nerd@gmail.com> - 2.23-1.fc3
- Updated to release 2.23.

* Sat Jul 29 2006 Dave M. <dave.nerd@gmail.com> - 2.22-1.fc3
- Added additional language support (ru_RU).

* Tue Jul 4 2006 Dave M. <dave.nerd@gmail.com> - 2.21-1.fc3
- Added additional language support (fr it).
- Updated to release 2.20.

* Wed Jun 14 2006 Dave M. <dave.nerd@gmail.com> - 2.20-1.fc3
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

* Sun Mar 20 2006 Dave M. <dave.nerd@gmail.com> - 2.16-1
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
