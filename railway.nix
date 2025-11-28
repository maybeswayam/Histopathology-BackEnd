{ pkgs }: {
  deps = [
    pkgs.libglvnd
    pkgs.glib
    pkgs.libxext
    pkgs.libxrender
    pkgs.libsm
    pkgs.libice
  ];
}
