%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}|perl\\((GSD!NDF|Starlink::AST)\\)

%define upstream_name    Astro-FITS-Header
%define upstream_version 3.07

Summary:	Interface to FITS headers
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Astro/%{upstream_name}-%{upstream_version}.tar.gz
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
%setup -qn %{upstream_name}-%{upstream_version}

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
