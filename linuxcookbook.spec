Summary:	LDP Linux Cookbook
Summary(pl.UTF-8):	Linuksowa książka kucharska
Name:		linuxcookbook
Version:	1.2
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/linuxcookbook/%{name}-%{version}.html.tar.gz
# Source0-md5:	876773dbb8c7b0b12951e939dfd5f0d7
URL:		http://www.tldp.org/LDP/linuxcookbook/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Over 1,500 time-saving recipes and hints for busy modern computer
users.

%description -l pl.UTF-8
Ponad 1500 przepisów i wskazówek oszczędzających czas dla zaganianych
użytkowników komputerów.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
