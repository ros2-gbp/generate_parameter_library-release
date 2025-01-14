%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-generate-parameter-library-py
Version:        0.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS generate_parameter_library_py package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-yaml
Requires:       python3-jinja2
Requires:       python3-typeguard
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python3-jinja2
BuildRequires:  python3-typeguard
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
%endif

%description
Python to generate ROS parameter library.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Jan 13 2025 Paul Gesel <paul.gesel@picknik.ai> - 0.4.0-1
- Autogenerated by Bloom

* Sun Oct 27 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.9-1
- Autogenerated by Bloom

* Wed Apr 03 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.8-3
- Autogenerated by Bloom

* Wed Apr 03 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.8-2
- Autogenerated by Bloom

* Fri Mar 08 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.8-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Paul Gesel <paul.gesel@picknik.ai> - 0.3.7-3
- Autogenerated by Bloom

