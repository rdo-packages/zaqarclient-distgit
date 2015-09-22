Name:           python-zaqarclient
Version:        0.2.0
Release:        1%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
Requires:       python-jsonschema
Requires:       python-keystoneclient >= 1.6.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-pbr
Requires:       python-requests >= 2.5.2
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.5.0

%description
Python client to Zaqar messaging service API v1

%prep
%setup -q

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst ChangeLog examples
%license LICENSE
%{python2_sitelib}/zaqarclient
%{python2_sitelib}/python_zaqarclient-*-py?.?.egg-info

%changelog
* Tue Sep 22 2015 Haikel Guemar <hguemar@fedoraproject.org> - 0.2.0-1
- Update to upstream 0.2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-3
- Drop PBR patch

* Mon Sep 29 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-2
- Drop PBR runtime dependency

* Sun Sep 28 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-1
- Initial package.
