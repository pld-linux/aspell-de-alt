Summary:	German (old spelling) dictionary for aspell
Summary(de.UTF-8):   Ein deutsches Wörterbuch (alter Spelling) für aspell
Summary(pl.UTF-8):   Niemiecki słownik ze starą pisownią dla aspella
Name:		aspell-de-alt
Version:	2.1
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/de/aspell6-de-alt-%{version}-%{subv}.tar.bz2
# Source0-md5:	13245374b03088608d729fd15c58cd7a
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
German (old spelling) dictionary (i.e. word list) for aspell.

%description -l de.UTF-8
Ein deutsches Wörterbuch (alter Spelling) zur Rechtschreibkontrolle
nach den neuen Rechtschreibregeln mit aspell.

%description -l pl.UTF-8
Niemiecki słownik (lista słów) ze starą pisownią dla aspella.

%prep
%setup -q -n aspell6-de-alt-%{version}-%{subv}

mv -f doc/{README,README.de}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%lang(de) %doc doc/README.de
%{_libdir}/aspell/*
%{_datadir}/aspell/*
