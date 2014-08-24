Name: clamtk
Version: 5.08
Release: 1.el7
Summary: Easy to use graphical user interface for Clam Antivirus (ClamAV) 
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://bitbucket.org/dave_theunsub/clamtk/

Source: https://bitbucket.org/dave_theunsub/clamtk/downloads/clamtk-%{version}.tar.gz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
Requires: perl(Gtk2) >= 1.248
Requires: clamav >= 0.95, clamav-update, data(clamav)
Requires: gnome-icon-theme, cronie
# Requires: nautilus-python

%description
ClamTk is a front end for ClamAV anti-virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{perl_vendorlib}/ClamTk

install -p -D -m0755 clamtk %{buildroot}/%{_bindir}/clamtk
# CentOS doesn't support this
# install -p -D -m0755 clamtk.py %{buildroot}/%{_datadir}/nautilus-python/extensions/%{name}.py
install -p -D -m0644 images/clamtk.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -p -D -m0644 clamtk.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
install -p -D -m0644 clamtk.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -p -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

# Install help files
# help/C/clamtk/figures
for dir in help/* ; do
	mkdir -p %{buildroot}/%{_datadir}/$dir/
	cp -a $dir/* %{buildroot}/%{_datadir}/$dir/%{name}
done

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

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc CHANGES DISCLAIMER LICENSE README

# The main executable
%{_bindir}/%{name}

# CentOS doesn't have this
# Nautilus extension executable
# %{_datadir}/nautilus-python/extensions/%{name}.py*

# Main Perl libraries
%{perl_vendorlib}/ClamTk

# Images
%{_datadir}/pixmaps/%{name}.png

# Desktop file
%{_datadir}/applications/%{name}.desktop

# Help files
#%{_datadir}/help/*/%{name}/

# Man pages
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Aug 24 2014 Dave M. <dave.nerd@gmail.com> - 5.08-1.el7
- Updated to release 5.08.
- Initial CentOS 7 release.
