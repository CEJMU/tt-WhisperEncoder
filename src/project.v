/*
 * tt_um_factory_test.v
 *
 * Test user module
 *
 * Author: Sylvain Munaut <tnt@246tNt.com>
 */

`default_nettype none

module tt_um_cejmu_wspr (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    assign uio_oe = 8'd255;
    assign uio_out[7:1] = 7'b0000000;

    toplevel_uart toplevel (
        .clk(clk),
        .reset(rst_n),
        .rx(ui_in[0]),
        .start_transmission(ui_in[1]),

        .encoding_valid(uo_out[0]),
        .cos_ds(uo_out[1]),
        .cos_ds_n(uo_out[2]),
        .sin_ds(uo_out[3]),
        .sin_ds_n(uo_out[4]),
        .lo_i(uo_out[5]),
        .lo_q(uo_out[6]),
        .lo_ix(uo_out[7]),
        .lo_qx(uio_out[0])
    );

endmodule  // tt_um_factory_test
