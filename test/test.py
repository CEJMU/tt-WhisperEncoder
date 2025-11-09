# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


async def send_byte(data, dut):
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 482)
    bits = bin(data)[2:].zfill(8)

    for bit in bits[::-1]:
        await ClockCycles(dut.clk, 241)
        dut.ui_in.value = int(bit)
        await ClockCycles(dut.clk, 241)

    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 482)


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 18, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 1
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    to_send = [
        0,
        0,
        0,
        10,
        53,
        80,
        11,
        37,
        96,
        12,
        78,
        64,
        13,
        75,
        72,
        14,
        75,
        192,
        1,
        0,
        2,
        2,
        22,
        60,
        3,
        128,
        28,
        4,
        29,
        109,
        5,
        128,
        28,
        6,
        36,
        158,
        7,
        128,
        28,
        8,
        43,
        206,
        9,
        128,
        28,
        0,
        0,
        1
    ]

    for i in to_send:
        await send_byte(i, dut)

    while dut.uo_out.value[0] == 0:
        await ClockCycles(dut.clk, 1)

    await ClockCycles(dut.clk, 10)
    dut.ui_in.value = 3
    await ClockCycles(dut.clk, 10)
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 100000)
