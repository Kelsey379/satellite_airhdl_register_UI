// // -----------------------------------------------------------------------------
// // 'DAMRegisterFilesPRESET' Register Definitions
// // Revision: 31
// // -----------------------------------------------------------------------------
// // Generated on 2023-06-02 at 01:54 (UTC) by airhdl version 2023.01.3-754176777
// // -----------------------------------------------------------------------------
// // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// // AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// // IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// // ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// // LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// // CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// // SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// // INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// // CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// // ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// // POSSIBILITY OF SUCH DAMAGE.
// // -----------------------------------------------------------------------------

// #ifndef DAMREGISTERFILESPRESET_REGS_H
// #define DAMREGISTERFILESPRESET_REGS_H

// #include <string>
// #include <cstdint>

// namespace DAMRegisterFilesPRESET_regs {

//     static const std::string name = "DAMRegisterFilesPRESET";

//     /* Revision number of the 'DAMRegisterFilesPRESET' register map */
//     static const std::uint32_t REVISION = 31;

//     /* Default base address of the 'DAMRegisterFilesPRESET' register map */
//     static const std::uint32_t BASE_ADDRESS = 0x4A000000;

//     /* Size of the 'DAMRegisterFilesPRESET' register map, in bytes */
//     static const std::uint32_t DAMREGISTERFILESPRESET_RANGE_BYTES = 16;

//     /* Register 'LEDs' */
//     static const std::uint32_t LEDS_OFFSET = 0x00000000; /* address offset of the 'LEDs' register */

//     /* Field 'LEDs.LED1' */
//     static const int LEDS_LED1_BIT_OFFSET = 0; /* bit offset of the 'LED1' field */
//     static const int LEDS_LED1_BIT_WIDTH = 1; /* bit width of the 'LED1' field */
//     static const std::uint32_t LEDS_LED1_BIT_MASK = 0x00000001; /* bit mask of the 'LED1' field */
//     static const std::uint32_t LEDS_LED1_RESET = 0x0; /* reset value of the 'LED1' field */

//     /* Field 'LEDs.LED2' */
//     static const int LEDS_LED2_BIT_OFFSET = 1; /* bit offset of the 'LED2' field */
//     static const int LEDS_LED2_BIT_WIDTH = 1; /* bit width of the 'LED2' field */
//     static const std::uint32_t LEDS_LED2_BIT_MASK = 0x00000002; /* bit mask of the 'LED2' field */
//     static const std::uint32_t LEDS_LED2_RESET = 0x0; /* reset value of the 'LED2' field */

//     /* Field 'LEDs.LED3' */
//     static const int LEDS_LED3_BIT_OFFSET = 2; /* bit offset of the 'LED3' field */
//     static const int LEDS_LED3_BIT_WIDTH = 1; /* bit width of the 'LED3' field */
//     static const std::uint32_t LEDS_LED3_BIT_MASK = 0x00000004; /* bit mask of the 'LED3' field */
//     static const std::uint32_t LEDS_LED3_RESET = 0x0; /* reset value of the 'LED3' field */

//     /* Field 'LEDs.LED4' */
//     static const int LEDS_LED4_BIT_OFFSET = 3; /* bit offset of the 'LED4' field */
//     static const int LEDS_LED4_BIT_WIDTH = 1; /* bit width of the 'LED4' field */
//     static const std::uint32_t LEDS_LED4_BIT_MASK = 0x00000008; /* bit mask of the 'LED4' field */
//     static const std::uint32_t LEDS_LED4_RESET = 0x0; /* reset value of the 'LED4' field */

//     /* Register 'VEn' */
//     static const std::uint32_t VEN_OFFSET = 0x00000004; /* address offset of the 'VEn' register */

//     /* Field 'VEn.ADC_1V8A' */
//     static const int VEN_ADC_1V8A_BIT_OFFSET = 0; /* bit offset of the 'ADC_1V8A' field */
//     static const int VEN_ADC_1V8A_BIT_WIDTH = 1; /* bit width of the 'ADC_1V8A' field */
//     static const std::uint32_t VEN_ADC_1V8A_BIT_MASK = 0x00000001; /* bit mask of the 'ADC_1V8A' field */
//     static const std::uint32_t VEN_ADC_1V8A_RESET = 0x0; /* reset value of the 'ADC_1V8A' field */

//     /* Field 'VEn.FEM_5VA' */
//     static const int VEN_FEM_5VA_BIT_OFFSET = 1; /* bit offset of the 'FEM_5VA' field */
//     static const int VEN_FEM_5VA_BIT_WIDTH = 1; /* bit width of the 'FEM_5VA' field */
//     static const std::uint32_t VEN_FEM_5VA_BIT_MASK = 0x00000002; /* bit mask of the 'FEM_5VA' field */
//     static const std::uint32_t VEN_FEM_5VA_RESET = 0x0; /* reset value of the 'FEM_5VA' field */

//     /* Field 'VEn.FEM_N5VA' */
//     static const int VEN_FEM_N5VA_BIT_OFFSET = 2; /* bit offset of the 'FEM_N5VA' field */
//     static const int VEN_FEM_N5VA_BIT_WIDTH = 1; /* bit width of the 'FEM_N5VA' field */
//     static const std::uint32_t VEN_FEM_N5VA_BIT_MASK = 0x00000004; /* bit mask of the 'FEM_N5VA' field */
//     static const std::uint32_t VEN_FEM_N5VA_RESET = 0x0; /* reset value of the 'FEM_N5VA' field */

//     /* Field 'VEn.HV_5VA' */
//     static const int VEN_HV_5VA_BIT_OFFSET = 3; /* bit offset of the 'HV_5VA' field */
//     static const int VEN_HV_5VA_BIT_WIDTH = 1; /* bit width of the 'HV_5VA' field */
//     static const std::uint32_t VEN_HV_5VA_BIT_MASK = 0x00000008; /* bit mask of the 'HV_5VA' field */
//     static const std::uint32_t VEN_HV_5VA_RESET = 0x0; /* reset value of the 'HV_5VA' field */

//     /* Register 'Clock_Low' */
//     static const std::uint32_t CLOCK_LOW_OFFSET = 0x00000008; /* address offset of the 'Clock_Low' register */

//     /* Field 'Clock_Low.value' */
//     static const int CLOCK_LOW_VALUE_BIT_OFFSET = 0; /* bit offset of the 'value' field */
//     static const int CLOCK_LOW_VALUE_BIT_WIDTH = 32; /* bit width of the 'value' field */
//     static const std::uint32_t CLOCK_LOW_VALUE_BIT_MASK = 0xFFFFFFFF; /* bit mask of the 'value' field */
//     static const std::uint32_t CLOCK_LOW_VALUE_RESET = 0x0; /* reset value of the 'value' field */

//     /* Register 'Clock_High' */
//     static const std::uint32_t CLOCK_HIGH_OFFSET = 0x0000000C; /* address offset of the 'Clock_High' register */

//     /* Field 'Clock_High.value' */
//     static const int CLOCK_HIGH_VALUE_BIT_OFFSET = 0; /* bit offset of the 'value' field */
//     static const int CLOCK_HIGH_VALUE_BIT_WIDTH = 32; /* bit width of the 'value' field */
//     static const std::uint32_t CLOCK_HIGH_VALUE_BIT_MASK = 0xFFFFFFFF; /* bit mask of the 'value' field */
//     static const std::uint32_t CLOCK_HIGH_VALUE_RESET = 0x0; /* reset value of the 'value' field */

// }

// #endif  /* DAMREGISTERFILESPRESET_REGS_H */