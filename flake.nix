{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { nixpkgs, rust-overlay, ... }:
    let
      # System types to support.
      supportedSystems = [
        "x86_64-linux"
      ];

      forAllSystems = function: nixpkgs.lib.genAttrs supportedSystems
        (system: function (import nixpkgs {
          inherit system;
          overlays = [ rust-overlay.overlays.default ];
        }));
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            nixpkgs-fmt
            rust-bin.stable.latest.default
          ];
        };
      });
    };
}
