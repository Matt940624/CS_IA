import { writable } from 'svelte/store'

export const isAuthenticated = writable(false);

export const signIn = () => {
    isAuthenticated.set(true);
}

export const signOut = () => {
    isAuthenticated.set(false);
}