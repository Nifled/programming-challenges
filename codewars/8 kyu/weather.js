/*
https://www.codewars.com/kata/55cb854deb36f11f130000e1
*/

const weatherInfo = temp => {
  const c = convertToCelsius(temp)
  return c < 0 ? `${c} is freezing temperature` : `${c} is above freezing temperature`
}

const convertToCelsius = temperature => {
  return (temperature - 32) * (5/9)
}
