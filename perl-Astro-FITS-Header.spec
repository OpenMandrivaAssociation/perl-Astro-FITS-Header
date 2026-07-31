%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}|perl\\((GSD!NDF|Starlink::AST)\\)

%define upstream_name    Astro-FITS-Header
Summary:	Interface to FITS headers
Name:		perl-%{upstream_name}
Version:	3.09
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Astro/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(JSON::PP)

%description
Stores information about a FITS header block in an object. Takes an hash
with an array reference as an arguement. The array should contain a list of
FITS header cards as input.

%prep
%setup -qn %{upstream_name}-%{version} -n Astro-FITS-Header-3.09

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*
