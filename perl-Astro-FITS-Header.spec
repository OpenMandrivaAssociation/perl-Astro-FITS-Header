%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Starlink::AST\\)|perl\\(NDF\\)|perl\\(Astro::FITS::CFITSIO\\)|perl\\(GSD\\)'
%else
%define _requires_exceptions Starlink::AST\\|NDF|Astro::FITS::CFITSIO\\|GSD
%endif

%define upstream_name    Astro-FITS-Header
%define upstream_version 3.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:    Interface to FITS headers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Astro/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch

%description
Stores information about a FITS header block in an object. Takes an hash
with an array reference as an arguement. The array should contain a list of
FITS header cards as input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.30.0-4mdv2012.0
+ Revision: 765066
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 3.30.0-2
+ Revision: 654221
- rebuild for updated spec-helper

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.30.0-1mdv2011.0
+ Revision: 628571
- update to new version 3.03

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.20.0-1mdv2011.0
+ Revision: 626875
- new version

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 3.10.0-1mdv2011.0
+ Revision: 574746
- import perl-Astro-FITS-Header

