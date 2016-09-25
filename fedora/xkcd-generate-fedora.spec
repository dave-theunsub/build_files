Name: xkcd-generate
Version: 0.0.7
Release: 1.fc
Summary: Generate pass phrases for authentication
License: GPL+ or Artistic 2.0
Group: Applications/System
URL: https://github.com/dave-theunsub/xkcd-generator

Source: https://github.com/dave-theunsub/xkcd-generator/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Gtk3)
Requires: perl-List-MoreUtils, perl-Getopt-Long

%description
Easily generate pass phrases for authentication using freely
available novels and dictionaries.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -D -m0755 xkcd-generate.pl $RPM_BUILD_ROOT%{_bindir}/xkcd-generate.pl
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
install -p -D -m0644 images/*.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
install -p -D -m0644 %{name}.pl.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.pl.1.gz

mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
install -p -D -m0644 sources/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
install -p -D -m0644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original                          \
        --add-category="GTK"                                    \
        --add-category="GNOME"                                  \
        --add-category="Utility"                                \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications          \
                $RPM_BUILD_ROOT/%{_datadir}/applications/*

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

# %files -f %{name}.lang
%files
%doc LICENSE CHANGES

# The main executable
%{_bindir}/*

# Images
%{_datadir}/pixmaps/*

# Desktop file
%{_datadir}/applications/*.desktop

# Source files
%{_defaultdocdir}/%{name}/*.txt
%{_defaultdocdir}/%{name}/*.dic

# Man pages
%{_mandir}/man1/*

%changelog
* Sun Sep 25 2016 Dave M <dave.nerd@gmail.com> - 0.0.7-1.fc
- New version.
- Remove perl-Math\* dependencies.

* Fri Sep 23 2016 Dave M <dave.nerd@gmail.com> - 0.0.6-1.fc
- Initial release for Fedora.
