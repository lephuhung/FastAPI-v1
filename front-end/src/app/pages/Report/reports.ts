export interface trichtin {
    uid : string
    ghichu_noidung : string
    nhanxet : string
    xuly: string
    uid_vaiao : string
    hoinhom_name?: string
    user: string
    created_at : string
    updated_at : string
}
export interface report {
    id: number
    social_account_uid: string
    content_note: string
    comment: string
    action: string
    related_social_account_uid: string
    created_at: string;
    updated_at: string;
    user: {
        id: string
        name: string
    } | null
}
type Report = {
    id: number;
    social_account_uid: string;
    content_note: string;
    comment: string;
    action: string;
    related_social_account_uid: string;
    created_at: string;
    updated_at: string;
    user: {
      id: string;
      name: string;
    } | null;
  }
