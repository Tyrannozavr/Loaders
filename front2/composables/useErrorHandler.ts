export function useErrorHandler(error: any, defaultMessage: string) {
  const message = error?.cause?._data?.message || defaultMessage;
  Notify.error(message);
}
