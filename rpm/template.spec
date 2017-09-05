Name:           ros-kinetic-velodyne-description
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS velodyne_description package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/velodyne_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin

%description
URDF and meshes describing Velodyne laser scanners.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Sep 05 2017 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.4-0
- Autogenerated by Bloom

* Sat Aug 13 2016 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.3-0
- Autogenerated by Bloom

