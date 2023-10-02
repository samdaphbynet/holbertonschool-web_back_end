// 6-final-user.js

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  try {
    const [user] = await Promise.all([userPromise, photoPromise]);
    return [{ user }, null];
  } catch (error) {
    return [null, error];
  }
}
