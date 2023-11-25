// RangeFilter.js
import { Box, NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper, Flex, Text } from '@chakra-ui/react';

const RangeFilter = ({ label, min, max, handleMin, handleMax }) => {


    return (
        <Box mt={5}>
            <Flex direction="row" gap={3}>
                <Flex align="center">
                    <Text mr={2}>Min {label}:</Text>
                    <NumberInput
                        onChange={(val) => handleMin(val)}
                        value={min}
                        max={100000}
                    >
                        <NumberInputField />
                        <NumberInputStepper>
                            <NumberIncrementStepper />
                            <NumberDecrementStepper />
                        </NumberInputStepper>
                    </NumberInput>
                </Flex>
                <Flex align="center">
                    <Text mr={2}>Max {label}:</Text>
                    <NumberInput
                        onChange={(val) => handleMax(val)}
                        value={max}
                        max={100000}
                    >
                        <NumberInputField />
                        <NumberInputStepper>
                            <NumberIncrementStepper />
                            <NumberDecrementStepper />
                        </NumberInputStepper>
                    </NumberInput>
                </Flex>
            </Flex>
        </Box>
    );
};

export default RangeFilter;
