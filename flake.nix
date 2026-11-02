{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        packages.design-pdf =
          pkgs.runCommand "design.md to pdf"
            {
              buildInputs = with pkgs; [
                typst
                pandoc
              ];
            }
            ''
              pandoc ${./DESIGN.md} \
                --pdf-engine typst \
                -V mainfont="sans-serif" \
                -o design.pdf

              mv design.pdf $out
            '';
      }
    );
}
