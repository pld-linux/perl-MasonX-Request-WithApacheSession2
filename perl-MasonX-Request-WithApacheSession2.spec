#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Request-WithApacheSession2
Summary:	MasonX::Request::WithApacheSession2 - add a session to the Mason Request object
Summary(pl):	MasonX::Request::WithApacheSession2 - dodawanie sesji do obiektu Mason Request
Name:		perl-MasonX-Request-WithApacheSession2
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e7446b6b0ab4f7b15a11217cc3177e4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache-mod_perl >= 1.99_1
BuildRequires:	perl(Apache::Cookie) >= 2.02-dev
BuildRequires:	perl(Apache::Request) >= 2.02-dev
BuildRequires:	perl-HTML-Mason >= 1.25
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MasonX::Request::WithApacheSession2 is a copy of the Mason module
MasonX::Request::WithApacheSession. With HTML::Mason::ApacheHandler2
Mason can run in a pure mod_perl2 environment.

MasonX::Request::WithApacheSession2 is highly experimental (alpha)
and should only be used in a test environment.

%description -l pl
MasonX::Request::WithApacheSession2 to kopia modu³u Masona
MasonX::Request::WithApacheSession. Przy u¿yciu
HTML::Mason::ApacheHandler2 Mason mo¿e dzia³aæ w ¶rodowisku czystego
mod_perl2.

Mason::Request::WithApacheSession2 jest bardzo eksperymentalny (alfa)
i powinien byæ u¿ywany tylko w ¶rodowiskach testowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
